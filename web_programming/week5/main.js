const MAP_CONTAINER_ID = 'map';
const GEOJSON_URL =
	'https://geo.stat.fi/geoserver/wfs?service=WFS&version=2.0.0&request=GetFeature&typeName=tilastointialueet:kunta4500k&outputFormat=json&srsName=EPSG:4326';
const MIGRATION_API_URL =
	'https://pxdata.stat.fi/PxWeb/api/v1/fi/StatFin/muutl/statfin_muutl_pxt_11a2.px';
const MIGRATION_QUERY_TEMPLATE_URL = './migration_data_query.json';

const map = L.map(MAP_CONTAINER_ID, {
	minZoom: -3,
});

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
	attribution:
		'&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
}).addTo(map);

let geoJsonLayer;

init().catch((error) => {
	console.error('Failed to initialize the map:', error);
});

async function init() {
	const [geoJsonData, migrationData] = await Promise.all([
		fetchGeoJson(),
		fetchMigrationStats(),
	]);

	const { stats, year } = migrationData;

	geoJsonLayer = L.geoJSON(geoJsonData, {
		style: (feature) => styleFeature(feature, stats),
		onEachFeature: (feature, layer) =>
			attachFeatureInteractions(feature, layer, stats, year),
	}).addTo(map);

	const bounds = geoJsonLayer.getBounds();
	if (bounds.isValid()) {
		map.fitBounds(bounds);
	}
}

async function fetchGeoJson() {
	const response = await fetch(GEOJSON_URL);
	if (!response.ok) {
		throw new Error(`Failed to fetch GeoJSON data: ${response.statusText}`);
	}
	return response.json();
}

async function fetchMigrationStats() {
	const [metadata, queryTemplate] = await Promise.all([
		fetch(MIGRATION_API_URL).then((response) => {
			if (!response.ok) {
				throw new Error(
					`Failed to fetch migration metadata: ${response.statusText}`,
				);
			}
			return response.json();
		}),
		fetch(MIGRATION_QUERY_TEMPLATE_URL).then((response) => {
			if (!response.ok) {
				throw new Error(
					`Failed to load migration query template: ${response.statusText}`,
				);
			}
			return response.json();
		}),
	]);

	const areaVariable = metadata.variables.find((variable) => variable.code === 'Alue');
	const yearVariable = metadata.variables.find((variable) => variable.code === 'Vuosi');

	if (!areaVariable || !yearVariable) {
		throw new Error('Unexpected migration metadata structure.');
	}

	const municipalityCodes = areaVariable.values.filter((code) => code !== 'SSS');
	const latestYear = yearVariable.values[yearVariable.values.length - 1];

	const query = JSON.parse(JSON.stringify(queryTemplate));
	query.query = query.query.map((entry) => {
		if (entry.code === 'Alue') {
			return {
				...entry,
				selection: {
					...entry.selection,
					values: municipalityCodes,
				},
			};
		}

		if (entry.code === 'Vuosi') {
			return {
				...entry,
				selection: {
					...entry.selection,
					values: [latestYear],
				},
			};
		}

		return entry;
	});

	const response = await fetch(MIGRATION_API_URL, {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json',
		},
		body: JSON.stringify(query),
	});

	if (!response.ok) {
		throw new Error(`Failed to fetch migration statistics: ${response.statusText}`);
	}

	const data = await response.json();
	const stats = buildMigrationStats(data);

	return { stats, year: latestYear };
}

function buildMigrationStats(data) {
	const areaIndex = data?.dimension?.Alue?.category?.index;
	const values = Array.isArray(data?.value) ? data.value : [];

	if (!areaIndex) {
		throw new Error('Migration statistics missing area index.');
	}

	const stats = {};

	Object.entries(areaIndex).forEach(([code, position]) => {
		const baseIndex = position * 2;
		const positive = toNumber(values[baseIndex]);
		const negative = toNumber(values[baseIndex + 1]);

		const municipalityCode = code.slice(2);
		stats[municipalityCode] = {
			positive,
			negative,
			net: positive - negative,
		};
	});

	return stats;
}

function styleFeature(feature, stats) {
	const municipalityCode = feature.properties?.kunta;
	const migration = municipalityCode ? stats[municipalityCode] : undefined;

	const positive = migration?.positive ?? 0;
	const negative = migration?.negative ?? 0;
	const hue = computeHue(positive, negative);

	return {
		weight: 2,
		color: '#ffffff',
		fillColor: Number.isFinite(hue)
			? `hsl(${hue}, 75%, 50%)`
			: 'hsl(0, 0%, 75%)',
		fillOpacity: 0.65,
	};
}

function attachFeatureInteractions(feature, layer, stats, year) {
	const name =
		feature.properties?.name || feature.properties?.nimi || 'Tuntematon kunta';
	const municipalityCode = feature.properties?.kunta;
	const migration = municipalityCode ? stats[municipalityCode] : undefined;

	layer.bindTooltip(name, { sticky: true });

	if (migration) {
		const { positive, negative, net } = migration;
		layer.bindPopup(
			`<strong>${name}</strong><br />` +
				`Vuosi: ${year}<br />` +
				`Tulomuutto: ${formatNumber(positive)}<br />` +
				`Lähtömuutto: ${formatNumber(negative)}<br />` +
				`Nettomuutto: ${formatNumber(net)}`,
		);
	} else {
		layer.bindPopup(`<strong>${name}</strong><br />Ei muuttotietoja`);
	}

	layer.on({
		mouseover: (event) => {
			const target = event.target;
			target.setStyle({ weight: 3 });
			target.bringToFront();
		},
		mouseout: (event) => {
			geoJsonLayer?.resetStyle(event.target);
		},
	});
}

function computeHue(positive, negative) {
	if (!Number.isFinite(positive) || positive < 0) {
		return 0;
	}

	if (!Number.isFinite(negative) || negative < 0) {
		return 120;
	}

	if (positive === 0 && negative === 0) {
		return 0;
	}

	if (negative === 0) {
		return 120;
	}

	const ratio = positive / negative;
	const hue = Math.pow(ratio, 3) * 60;
	return Math.min(120, Math.max(0, hue));
}

function toNumber(value) {
	return typeof value === 'number' && Number.isFinite(value) ? value : 0;
}

function formatNumber(value) {
	const number = Number(value);
	return Number.isFinite(number) ? number.toLocaleString('fi-FI') : '0';
}

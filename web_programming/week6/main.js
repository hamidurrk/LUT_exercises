let populationData = [];
let currentMunicipality = 'SSS'; 
let municipalityCodes = {};
let chart;

const years = ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021'];

async function fetchMunicipalityCodes() {
    try {
        const response = await fetch('https://statfin.stat.fi/PxWeb/api/v1/en/StatFin/synt/statfin_synt_pxt_12dy.px');
        const data = await response.json();

        const alueData = data.variables[1];
        const codes = alueData.values;
        const names = alueData.valueTexts; 

        for (let i = 0; i < names.length; i++) {
            municipalityCodes[names[i].toLowerCase()] = codes[i];
        }
    } catch (error) {
        console.error('Error fetching municipality codes:', error);
    }
}

async function fetchPopulationData(municipalityCode = 'SSS') {
    const requestBody = {
        "query": [
            {
                "code": "Vuosi",
                "selection": {
                    "filter": "item",
                    "values": years
                }
            },
            {
                "code": "Alue",
                "selection": {
                    "filter": "item",
                    "values": [municipalityCode]
                }
            },
            {
                "code": "Tiedot",
                "selection": {
                    "filter": "item",
                    "values": ["vaesto"]
                }
            }
        ],
        "response": {
            "format": "json-stat2"
        }
    };

    try {
        const response = await fetch('https://statfin.stat.fi/PxWeb/api/v1/en/StatFin/synt/statfin_synt_pxt_12dy.px', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        const data = await response.json();

        populationData = data.value;
        currentMunicipality = municipalityCode;

        localStorage.setItem('currentMunicipality', municipalityCode);

        return populationData;
    } catch (error) {
        console.error('Error fetching population data:', error);
        return [];
    }
}

function createChart(data, title = 'Population Growth') {
    const chartData = {
        labels: years,
        datasets: [{
            name: 'Population',
            values: data,
            chartType: 'line'
        }]
    };

    const chartConfig = {
        title: title,
        data: chartData,
        type: 'line',
        height: 450,
        colors: ['#eb5146'],
        axisOptions: {
            xAxisMode: 'tick'
        }
    };

    if (chart) {
        chart.update(chartData);
    } else {
        chart = new frappe.Chart('#chart', chartConfig);
    }
}

async function init() {
    await fetchMunicipalityCodes();
    const data = await fetchPopulationData();
    createChart(data, 'Population Growth - Whole Country');
}

document.addEventListener('DOMContentLoaded', init);

document.getElementById('submit-data').addEventListener('click', async () => {
    const input = document.getElementById('input-area').value.trim().toLowerCase();
    const code = municipalityCodes[input];

    if (code) {
        const data = await fetchPopulationData(code);
        const municipalityName = Object.keys(municipalityCodes).find(key => municipalityCodes[key] === code);
        createChart(data, `Population Growth - ${municipalityName.charAt(0).toUpperCase() + municipalityName.slice(1)}`);
    } else {
        alert('Municipality not found. Please check the spelling.');
    }
});

document.getElementById('add-data').addEventListener('click', () => {
    if (populationData.length < 2) return;

    const deltas = [];
    for (let i = 1; i < populationData.length; i++) {
        deltas.push(populationData[i] - populationData[i - 1]);
    }

    const meanDelta = deltas.reduce((sum, delta) => sum + delta, 0) / deltas.length;

    const prediction = populationData[populationData.length - 1] + meanDelta;
    populationData.push(prediction);
    years.push((parseInt(years[years.length - 1]) + 1).toString());

    createChart(populationData, chart.title || 'Population Growth');
});

const API_ENDPOINT = "https://api.tvmaze.com/search/shows?q=";

const init = () => {
	const form = document.getElementById("search-form");
	const input = document.getElementById("input-show");
	const resultsContainer = document.querySelector(".show-container");

	if (!form || !input || !resultsContainer) {
		return;
	}

	const urlParams = new URLSearchParams(window.location.search);
	const initialQuery = urlParams.get("q");

	if (initialQuery) {
		input.value = initialQuery;
		fetchShows(initialQuery, resultsContainer);
	}

	form.addEventListener("submit", (event) => {
		event.preventDefault();
		const query = input.value.trim();

		if (!query) {
			renderMessage("Please enter a search term to get started.", "empty-state", resultsContainer);
			return;
		}

		urlParams.set("q", query);
		const newUrl = `${window.location.pathname}?${urlParams.toString()}`;
		window.history.replaceState({}, "", newUrl);

		fetchShows(query, resultsContainer);
	});
};

async function fetchShows(query, container) {
	renderMessage("Loading shows…", "empty-state", container);

	try {
		const response = await fetch(`${API_ENDPOINT}${encodeURIComponent(query)}`);
		if (!response.ok) {
			throw new Error(`Request failed with status ${response.status}`);
		}

		const data = await response.json();
		renderShows(Array.isArray(data) ? data : [], container);
	} catch (error) {
		renderMessage(
			"Something went wrong while fetching shows. Please try again.",
			"error-state",
			container
		);
		console.error(error);
	}
}

function renderShows(shows, container) {
	container.innerHTML = "";

	if (!shows.length) {
		renderMessage("No shows found. Try another search term!", "empty-state", container);
		return;
	}

	const fragment = document.createDocumentFragment();

	shows.forEach((item) => {
		const show = item.show;
		if (!show) {
			return;
		}

		const showCard = document.createElement("div");
		showCard.className = "show-data";

		const imageElement = document.createElement("img");
		imageElement.src = show.image?.medium || "https://via.placeholder.com/210x295?text=No+Image";
		imageElement.alt = show.name ? `${show.name} poster` : "Show poster unavailable";

		const infoContainer = document.createElement("div");
		infoContainer.className = "show-info";

		const titleElement = document.createElement("h1");
		titleElement.textContent = show.name || "Untitled Show";

		const summaryWrapper = document.createElement("div");
		summaryWrapper.innerHTML = show.summary || "<p>No summary available.</p>";

		infoContainer.appendChild(titleElement);
		infoContainer.appendChild(summaryWrapper);

		showCard.appendChild(imageElement);
		showCard.appendChild(infoContainer);

		fragment.appendChild(showCard);
	});

	container.appendChild(fragment);
}

function renderMessage(message, className, container) {
	container.innerHTML = "";
	const messageElement = document.createElement("div");
	messageElement.className = className;
	messageElement.textContent = message;
	container.appendChild(messageElement);
}

if (document.readyState === "loading") {
	document.addEventListener("DOMContentLoaded", init);
} else {
	init();
}

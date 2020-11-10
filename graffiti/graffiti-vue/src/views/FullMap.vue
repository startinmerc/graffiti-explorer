<template>
	<main class="page">
		<div id="map-container"></div>
	</main>
</template>

<script>
import Vue from "vue";
import mapboxgl from "mapbox-gl";
import { geoData } from "../../data";
// Import popup component & create class for mounting
import ArtworkPopup from "../components/ArtworkPopup";
const ArtworkPopupClass = Vue.extend(ArtworkPopup);

export default {
	name: "FullMap",

	mounted() {
		// Get API token from .env
		mapboxgl.accessToken = process.env.VUE_APP_MAPBOX_TOKEN;

		// Load map
		this.loadMap().then((mapBox) => {
			// Add points
			this.addPoints(mapBox);
			// Add layer with points
			this.addLayer(mapBox);
			// Add interactions
			this.addMouseInteraction(mapBox);
		});
	},
	methods: {
		loadMap() {
			// Async loading function to await styles
			return new Promise((resolve) => {
				// Create Map
				let mapBox = new mapboxgl.Map({
					// Target div id
					container: "map-container",
					// Custom mapbox style
					style: "mapbox://styles/startinmerc/ckh3c2oam2izs19nknv2xyviy",
					// !-Arbitrary, to change to auto-fit points
					center: [-1.080278, 53.958332],
					// !-Arbitrary, to change to auto-fit points
					zoom: 13,
				});
				// Resolve Promise when styling is loaded
				mapBox.on("styledata", () => {
					// Send mapBox to pass through to other methods
					resolve(mapBox);
				});
			});
		},
		addPoints(mapBox) {
			// !-Import geoJSON from testData
			mapBox.addSource("artworks", geoData);
		},
		addLayer(mapBox) {
			mapBox.addLayer({
				id: "artworks",
				type: "symbol",
				source: "artworks",
				layout: {
					// SVG file loaded into Mapbox Studio style
					"icon-image": "ArtworkMarker",
					// Allow icons to be visible over other icons
					"icon-allow-overlap": true,
					// Why, Mapbox, did it take me an hour to find this property in your docs?
					"icon-anchor": "bottom",
				},
			});
		},
		addMouseInteraction(mapBox) {
			mapBox.on("click", "artworks", (e) => {
				// Coordinates from event
				var coordinates = e.features[0].geometry.coordinates.slice();
				// Data from event trigger
				var title = e.features[0].properties.title;
				var artist = e.features[0].properties.artist;
				var id = e.features[0].properties.id;

				const popup = new mapboxgl.Popup()
					.setLngLat(coordinates)
					// Set HTML as Vue ref div
					.setHTML('<div id="vue-popup-content"></div>')
					.addTo(mapBox);

				// Create new Vue component with props for Popup
				const popupInstance = new ArtworkPopupClass({
					propsData: {
						title: title,
						artist: artist,
						id: id,
					},
				});

				// Center map on selcted point
				mapBox.flyTo({
					center: e.features[0].geometry.coordinates,
					speed: 0.8,
				});

				// Mount Vue component within the Vue ref div created earlier
				popupInstance.$mount("#vue-popup-content");

				// Update popup after adding content to resize
				popup._update();
			});

			// Change the cursor to a pointer when the mouse is over the artworks layer.
			mapBox.on("mouseenter", "artworks", function() {
				mapBox.getCanvas().style.cursor = "pointer";
			});

			// Change it back to a pointer when it leaves.
			mapBox.on("mouseleave", "artworks", function() {
				mapBox.getCanvas().style.cursor = "";
			});
		},
	},
};
</script>

<style scoped>
#map-container {
	width: 100%;
	height: 100vh;
}
</style>

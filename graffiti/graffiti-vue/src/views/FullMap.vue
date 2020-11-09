<template>
	<main>
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
				let mapBox = new mapboxgl.Map({
					container: "map-container",
					// Custom mapbox style
					style: "mapbox://styles/startinmerc/ckh3c2oam2izs19nknv2xyviy",
					// Arbitrary, to change to auto-fit points
					center: [-1.07825, 53.95798],
					// Arbitrary, to change to auto-fit points
					zoom: 13,
				});
				mapBox.on("styledata", () => {
					resolve(mapBox);
				});
			});
		},
		addPoints(mapBox) {
			// Import geoJSON
			mapBox.addSource("places", geoData);
		},
		addLayer(mapBox) {
			mapBox.addLayer({
				id: "places",
				type: "symbol",
				source: "places",
				layout: {
					// To change to custom eye marker
					"icon-image": "{icon}-15",
					"icon-allow-overlap": true,
				},
			});
		},
		addMouseInteraction(mapBox) {
			mapBox.on("click", "places", (e) => {
				var coordinates = e.features[0].geometry.coordinates.slice();
				var name = e.features[0].properties.name;

				// Ensure that if the map is zoomed out such that multiple
				// copies of the feature are visible, the popup appears
				// over the copy being pointed to.
				while (Math.abs(e.lngLat.lng - coordinates[0]) > 180) {
					coordinates[0] += e.lngLat.lng > coordinates[0] ? 360 : -360;
				}

				const popup = new mapboxgl.Popup()
					.setLngLat(coordinates)
					.setHTML('<div id="vue-popup-content"></div>')
					.addTo(mapBox);

				// create a new Vue component with your props for this Popup
				const popupInstance = new ArtworkPopupClass({
					propsData: {
						title: name,
					},
				});

				// mount this Vue component within the empty div Mapbox GL JS has just
				// created in the DOM
				popupInstance.$mount("#vue-popup-content");

				// since the size of the popup may have changed when mounting the Vue
				// component, force an update for dynamic positioning
				popup._update();
			});

			// Change the cursor to a pointer when the mouse is over the places layer.
			mapBox.on("mouseenter", "places", function() {
				mapBox.getCanvas().style.cursor = "pointer";
			});

			// Change it back to a pointer when it leaves.
			mapBox.on("mouseleave", "places", function() {
				mapBox.getCanvas().style.cursor = "";
			});
		},
	},
};
</script>

<style scoped>
.marker {
	margin: 0;
}
#map-container {
	width: 100%;
	height: 100vh;
}
</style>

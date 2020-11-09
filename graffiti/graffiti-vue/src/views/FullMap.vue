<template>
	<main>
		<div id="map-container"></div>
	</main>
</template>

<script>
import mapboxgl from "mapbox-gl";
import { geoData } from "../../data";

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

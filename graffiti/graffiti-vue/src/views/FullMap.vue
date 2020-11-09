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
		mapboxgl.accessToken = process.env.VUE_APP_MAPBOX_TOKEN;

		var map = new mapboxgl.Map({
			container: "map-container",
			style: "mapbox://styles/startinmerc/ckh3c2oam2izs19nknv2xyviy",
			center: [-1.07825, 53.95798],
			zoom: 13,
		});

		// add markers...
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

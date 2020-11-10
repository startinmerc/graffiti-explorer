<template>
	<main>
		<!-- Show photo if found -->
		<img v-if="photo" :src="photo" alt="artwork" />
		<!-- Otherwise show placeholder -->
		<div v-else class="placeholder"></div>
		<div class="padded">
			<h1>{{ title }}</h1>
			<b>{{ artist }}</b>
			<p>{{ description }}</p>
			<router-link to="/map"><button>Back to map</button></router-link>
		</div>
	</main>
</template>

<script>
import { geoData } from "../../data";

export default {
	name: "ArtworkDetail",
	data: function() {
		return {
			title: "Artwork Title",
			artist: "Artwork Artist",
			description: "Artwork Description",
			photo: false,
		};
	},
	mounted() {
		// If title (therefore others) not present...
		if (!this.$route.params.title) {
			// Find in geoData based on id from param
			let res = geoData.data.features.find(
				(v) => v.properties.id === this.$route.params.id
			);
			// If nothing found, break
			if (!res) {
				return;
			}

			// Set data to found properties
			this.title = res.properties.title;
			this.description = res.properties.description;
			this.artist = res.properties.artist;
			this.photo = res.properties.photos;
		} else {
			// Set data to param properties
			this.title = this.$route.params.title;
			this.description = this.$route.params.description;
			this.artist = this.$route.params.artist;
			this.photo = this.$route.params.photos;
		}
	},
};
</script>

<style scoped>
img {
	width: auto;
	max-height: 40vh;
	margin: 0 auto;
	display: block;
}
.placeholder {
	height: 50vh;
}
</style>

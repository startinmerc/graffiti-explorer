<template>
	<main>
		<img :src="$route.params.photo || photo" alt="artwork" />
		<h1>{{ $route.params.title || title }}</h1>
		<b>{{ $route.params.artist || artist }}</b>
		<p>{{ $route.params.description || description }}</p>
		<router-link to="/map"><button>Back to map</button></router-link>
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
			photo: "Artwork photo",
		};
	},
	mounted() {
		if (!this.$route.params.title) {
			try {
				let res = geoData.data.features.find(
					(v) => v.properties.id === this.$route.params.id
				);
				this.title = res.properties.title;
				this.description = res.properties.description;
				this.artist = res.properties.artist;
				this.photo = res.properties.photos;
			} catch (error) {
				console.log(error);
			}
		}
	},
};
</script>

<style scoped>
img {
	width: 100%;
	height: auto;
}
.placeholder {
	height: 50vh;
}
</style>

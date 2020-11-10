<template>
	<main>
		<img :src="$route.params.photo" alt="artwork"/>
		<!-- <div class="placeholder"></div> -->
		<h1>{{ $route.params.title||title }}</h1>
		<b>{{ $route.params.artist||artist }}</b>
		<p>{{ $route.params.description||description }}</p>
		<router-link to="/map"><button>Back to map</button></router-link>
	</main>
</template>

<script>
export default {
	name: "ArtworkDetail",
	props: {
		title: {type: String, default: "Artwork Title"},
		artist: {type: String, default: "Artwork Artist"},
		description: {type: String, default: "Artwork Description"},
	},
	mounted(){
		console.log(this.$route.params)
	}
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
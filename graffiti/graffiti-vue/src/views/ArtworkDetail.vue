<template>
	<main>
		<div class="placeholder"></div>
		<h1>{{ title }}</h1>
		<b>Artist</b>
		<p>{{ description }}</p>
		<router-link to="/map"><button>Back to map</button></router-link>
	</main>
</template>

<script>
export default {
	name: "ArtworkDetail",
	props: {
		title: {type: String, default: "Artwork Title"},
		description: {type: String, default: "Artwork Description"},
	},
};
</script>

<style scoped>
main {
  /* Rough estimate of header, needs to be found in window */
  margin-top: 90px;
}
.placeholder {
  height: 50vh;
}
</style>
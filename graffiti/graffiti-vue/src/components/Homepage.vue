<template>
	<main>
		<div>
			<h1>York<br />Graffiti<br />Explorer</h1>
			<button>View the map</button>
		</div>
	</main>
</template>

<script>
export default {
	name: "Homepage",
};
</script>

<style scoped lang="scss">
main {
	height: 100vh;
	background: pink;
	text-align: center;
	color: var(--red);
	h1 {
		font-size: 4rem;
		background: var(--darkblue);
		padding: 2rem;
		display: inline-block;
		margin-top: 15vh;
		margin-bottom: 10vh;
		text-align: left;
	}
}
</style>

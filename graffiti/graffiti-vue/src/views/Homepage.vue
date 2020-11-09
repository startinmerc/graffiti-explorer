<template>
	<main>
		<div>
			<h1>
				York<br />
				Graffiti<br />
				Explorer
			</h1>
			<router-link to="/map">
				<button>
					View the map
					<icon-base icon-name="arrow-right">
						<ArrowRight />
					</icon-base>
				</button>
			</router-link>
		</div>
	</main>
</template>

<script>
import IconBase from "../components/icons/IconBase";
import ArrowRight from "../components/icons/ArrowRight";
export default {
	name: "Homepage",
	components: {
		IconBase,
		ArrowRight,
	},
};
</script>

<style scoped lang="scss">
main {
	height: 100vh;
	text-align: center;
	color: var(--red);
	overflow: hidden;
	background: no-repeat center center;
	background-image: url("../assets/Homepage.jpg");
	background-size: cover;
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

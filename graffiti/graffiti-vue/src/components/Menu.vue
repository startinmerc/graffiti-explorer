<template>
	<nav>
		<p id="nav-logo">
			<router-link to="/">York<br />Graffiti<br />Explorer</router-link>
		</p>
		<router-link to="/about">
			<button>
				<icon-base icon-name="hamburger" width="36" height="36">
					<Hamburger />
				</icon-base>
			</button>
		</router-link>
	</nav>
</template>

<script>
import IconBase from "./icons/IconBase";
import Hamburger from "./icons/Hamburger";

export default {
	name: "Menu",
	components: {
		IconBase,
		Hamburger,
	},
};
</script>

<style lang="scss">
nav {
	position: absolute;
	top: 0;
	left: 0;
	z-index: 100;
	width: calc(100% - 2rem);
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: 1rem;
	background-color: var(--darkblue);
	color: var(--red);
	#nav-logo {
		margin: 0;
	}
	#nav-logo * {
		color: var(--red);
		text-decoration: none;
	}
	ul {
		position: absolute;
	}
	button {
		// border: 1px solid var(--red);
	}
}
</style>

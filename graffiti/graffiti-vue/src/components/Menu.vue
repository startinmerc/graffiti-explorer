<template>
	<nav>
		<p id="nav-logo">
			<router-link to="/">York<br />Graffiti<br />Explorer</router-link>
		</p>
		<button @click="toggleMenu">
			<icon-base icon-name="hamburger" width="36" height="36">
				<Hamburger />
			</icon-base>
		</button>
		<transition name="menuSlide">
		<ul v-if="menuOpen">
			<li><router-link to="">Home</router-link></li>
			<li><router-link to="/map">Map</router-link></li>
			<li><router-link to="/about">About</router-link></li>
		</ul>
		</transition>
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
	data: function() {
		return {
			menuOpen: false,
		};
	},
	methods: {
		toggleMenu() {
			this.menuOpen = !this.menuOpen;
		},
	},
};
</script>

<style lang="scss">
nav {
	position: sticky;
	top: 0;
	left: 0;
	z-index: 1;
	height: 60px;
	width: calc(100% - var(--padding) * 2);
	display: flex;
	justify-content: space-between;
	align-items: center;
	padding: var(--padding);
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
		z-index: -100;
		top: 100%;
		left: 0;
		margin: 0;
		padding: 0;
		width: 100%;
		list-style: none;
		li {
			a {
				border-top: 1px solid var(--red);
				padding: var(--padding);
				display: inline-block;
				color: var(--red);
				background-color: var(--darkblue);
				width: 100%;
			}
		}
	}
}
	}
	button {
		// border: 1px solid var(--red);
	}
}
</style>

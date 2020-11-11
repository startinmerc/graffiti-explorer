<template>
	<nav>
		<p id="nav-logo">
			<router-link to="/">York<br />Graffiti<br />Explorer</router-link>
		</p>
		<button @click="toggleMenu">
			<MenuIcon :menuOpen="menuOpen" />
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
import MenuIcon from "./MenuIcon";

export default {
	name: "Menu",
	components: {
		MenuIcon,
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
		a {
			text-decoration: none;
		}
	}
	ul {
		position: absolute;
		top: 100%;
		right: 0;
		width: 50%;
		height: calc(100vh - 90px);
		background: var(--darkblue);
		margin: 0;
		padding: 0;
		list-style: none;
		font-size: 1.3rem;
		li {
			a {
				padding: var(--padding);
				display: inline-block;
				color: var(--red);
				background-color: var(--darkblue);
				width: calc(100% - 30px);
				&:hover {
					color: var(--white);
				}
			}
		}
	}
}

// Add classes
.menuSlide-enter-active {
	animation: slideIn 210ms ease-in forwards;
}
.menuSlide-leave-active {
	animation: slideOut 210ms ease-in forwards;
}

@keyframes slideIn {
	from {
		transform: translateX(100%);
	}
	to {
		transform: translateX(0%);
	}
}

@keyframes slideOut {
	from {
		transform: translateX(0%);
	}
	to {
		transform: translateX(100%);
	}
}
</style>

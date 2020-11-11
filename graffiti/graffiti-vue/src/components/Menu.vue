<template>
	<nav>
		<p id="nav-logo">
			<router-link to="/">York<br />Graffiti<br />Explorer</router-link>
		</p>
		<button @click="toggleMenu">
			<MenuIcon :menuOpen="menuOpen" />
		</button>
		<transition name="menuSlide">
			<ul v-if="menuOpen" @click="toggleMenu">
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
		// Darkened background for expanded menu
		// !-z-indexing issue on leave
		&::before {
			content: "";
			position: absolute;
			top: 0;
			left: -100%;
			height: 100%;
			width: 200%;
			background-color: var(--black);
			opacity: 0.2;
			z-index: -1;
		}
	}
}

// ================= Transitions =================

.menuSlide-enter-active {
	animation: slideIn 210ms ease-in forwards;
	&::before {
		animation: pseudoIn 210ms ease-in forwards;
	}
}
.menuSlide-leave-active {
	animation: slideOut 210ms ease-in forwards;
	&::before {
		animation: pseudoOut 210ms ease-in forwards;
	}
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

@keyframes pseudoIn {
	from {
		transform: translateX(-50%);
		opacity: 0;
	}
	to {
		transform: translateX(0%);
		opacity: 0.2;
	}
}

@keyframes pseudoOut {
	from {
		transform: translateX(0%);
		opacity: 0.2;
	}
	to {
		transform: translateX(-50%);
		opacity: 0;
	}
}
</style>

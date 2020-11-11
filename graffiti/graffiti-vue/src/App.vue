<template>
	<div id="app">
		<Menu />
		<transition :name="transitionName">
			<router-view />
		</transition>
	</div>
</template>

<script>
import Menu from "./components/Menu.vue";

export default {
	name: "App",
	components: {
		Menu,
	},
	data() {
		return {
			transitionName: "",
		};
	},
	watch: {
		$route(to, from) {
			function direction(to, from) {
				let last = from.path.split("/")[from.path.split("/").length - 1];
				let dest = to.path.split("/")[to.path.split("/").length - 1];

				if (
					dest === "" ||
					last === "about" ||
					(dest === "map" &&
						from.path.split("/")[from.path.split("/").length - 2] === "artwork")
				) {
					return "left";
				}
				return "right";
			}

			this.transitionName = `swipe-${direction(to, from)}`;
		},
	},
};
</script>

<style lang="scss">
// ============== Root Variables ==============

:root {
	--darkblue: #33405c;
	--lightblue: #afdee4;
	--yellow: #fef05b;
	--red: #e14e6d;
	--black: #221e1d;
	--white: #f9f9f9;
	--padding: 15px;
}

// =============== Style resets ===============

body {
	font-family: "Raleway", sans-serif;
	margin: 0;
}

button {
	border: 0;
	border-radius: 500rem;
	background: var(--darkblue);
	color: var(--red);
	font-family: inherit;
	font-size: inherit;
	line-height: 1.2;
	white-space: nowrap;
	text-decoration: none;
	padding: 0.25rem 0.5rem;
	margin: 0.25rem;
	cursor: pointer;
	transition: color 80ms ease-in;

	&:hover {
		color: var(--white);
	}
}

// =============== Global Elements ===============

main {
	position: absolute;
	top: 90px;
	width: 100%;
	min-height: calc(100% - 90px);
}

// =============== Helper classes ===============

.padded {
	padding: 0 var(--padding);
}

// ============== Page Transitions ==============

.page-fade-enter-active {
	animation: coming 180ms ease-in;
}
.page-fade-leave-active {
	animation: going 180ms ease-in;
}

@keyframes going {
	from {
		opacity: 1;
	}
	to {
		opacity: 0;
	}
}

@keyframes coming {
	from {
		opacity: 0;
	}
	to {
		opacity: 1;
	}
}
</style>

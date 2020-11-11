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

a {
	transition: all 80ms ease-out;
	color: var(--red);
	&:hover,
	&:active {
		background-color: var(--darkblue);
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

:root {
	--page-time: 210ms;
	--page-easing: cubic-bezier(0.19, 1, 0.22, 1);
}

.swipe-right-enter-active {
	animation: rightComing var(--page-time) var(--page-easing);
}
.swipe-right-leave-active {
	animation: rightGoing var(--page-time) var(--page-easing);
}

@keyframes rightGoing {
	from {
		transform: translateX(0);
	}
	to {
		transform: translateX(-100%);
	}
}

@keyframes rightComing {
	from {
		transform: translateX(100%);
	}
	to {
		transform: translateX(0%);
	}
}

.swipe-left-enter-active {
	animation: leftComing var(--page-time) var(--page-easing);
}
.swipe-left-leave-active {
	animation: leftGoing var(--page-time) var(--page-easing);
}

@keyframes leftGoing {
	from {
		transform: translateX(0);
	}
	to {
		transform: translateX(100%);
	}
}

@keyframes leftComing {
	from {
		transform: translateX(-100%);
	}
	to {
		transform: translateX(0%);
	}
}

</style>

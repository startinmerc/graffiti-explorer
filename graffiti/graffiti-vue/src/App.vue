<template>
	<div id="app">
		<Homepage />
	</div>
</template>

<script>
import Homepage from "./components/Homepage.vue";

export default {
	name: "App",
	components: {
		Homepage,
	},
};
</script>

<style>
:root {
	--darkblue: #33405c;
	--lightblue: #afdee4;
	--yellow: #fef05b;
	--red: #e14e6d;
	--black: #221e1d;
	--white: #f9f9f9;
}

/* Style resets */
body {
	font-family: "Raleway", sans-serif;
	margin: 0;
}
#app {
  overflow: hidden;
  max-width: 100vw;
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
}
</style>
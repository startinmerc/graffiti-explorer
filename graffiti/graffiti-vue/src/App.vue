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
  --darkblue: #33405C;
  --lightblue: #AFDEE4;
  --yellow: #FEF05B;
  --red: #E14E6D;
  --black: #221E1D;
  --white: #F9F9F9;
}

/* Style resets */
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
}

</style>

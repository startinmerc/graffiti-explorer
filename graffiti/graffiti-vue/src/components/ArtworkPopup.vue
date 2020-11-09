<template>
	<div class="artwork-popup">
		<div class="placeholder"></div>
		<h3>{{ title }}</h3>
		<p>Artist</p>
		<button>
			View Detail
			<icon-base icon-name="arrow-right" height="15" width="15">
				<ArrowRight />
			</icon-base>
		</button>
	</div>
</template>

<script>
import IconBase from "./icons/IconBase";
import ArrowRight from "./icons/ArrowRight";
export default {
	name: "ArtworkPopup",
	props: {
		title: String,
	},
	components: {
		IconBase,
		ArrowRight,
	},
};
</script>

<style lang="scss">
// Placeholder for artwork image
.placeholder {
	height: 50px;
	// Widen to compensate for .mapbox-popup-content padding
	width: calc(100% + 20px);
	margin-left: -10px;
	margin-top: -10px;
	// Gradient backgrounds
	background-image: linear-gradient(132.18deg, #33405c 0%, #afdee4 100%);
}
</style>

<template>
	<div class="artwork-popup">
		<div class="placeholder"></div>
		<h3>{{ title }}</h3>
		<p>{{ artist }}</p>
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
		artist: String,
		id: String,
	},
	components: {
		IconBase,
		ArrowRight,
	},
};
</script>

<style lang="scss">
.mapboxgl-popup {
	--padding: 5px;
	padding-bottom: 20px;
}
.mapboxgl-popup-tip {
	display: none;
}
.mapboxgl-popup-content {
	padding: var(--padding);
	border-radius: 0;
	button {
		margin: 0;
	}
	h3,
	p {
		margin: var(--padding) 0;
	}
	h3 {
		color: var(--red);
	}
}
.mapboxgl-popup-close-button {
	margin: 0;
}
// Placeholder for artwork image
.placeholder {
	min-height: 50px;
	// Widen to compensate for .mapbox-popup-content padding
	width: calc(100% + var(--padding) * 2);
	margin-left: calc(0px - var(--padding));
	margin-top: calc(0px - var(--padding));
	// Gradient backgrounds
	background-image: linear-gradient(132.18deg, #33405c 0%, #afdee4 100%);
}
</style>

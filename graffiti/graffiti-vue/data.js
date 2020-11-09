export const testData = [
	{ title: "test data 1", location: [-1.077706, 53.956799] },
	{ title: "test data 2", location: [-1.086944, 53.957329] },
	{ title: "test data 3", location: [-1.088489, 53.959355] },
	{ title: "test data 4", location: [-1.087631, 53.96402] },
	{ title: "test data 5", location: [-1.082696, 53.964108] },
];

function buildJSON(data) {
	let features = data.map((v) => ({
		type: "Feature",
		geometry: {
			type: "Point",
			coordinates: v.location,
		},
		properties: {
			name: v.title,
			icon: "rocket",
		},
	}));
	return {
		type: "geojson",
		data: { type: "FeatureCollection", features: features },
	};
}

export const geoData = buildJSON(testData);

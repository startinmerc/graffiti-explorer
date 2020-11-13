# York Graffiti Explorer

A mobile-first site using Vue and Mapbox

---

## To Do - Front end

- Add axios calls to api
- Change page transitions to slide reveal?

## To do - Back end

- Change api response to geoJSON
- Implement validation on model fields
- Swap dbs?

---

### Front end dev setup

(Assuming vue cli is installed)

```bash
cd graffiti/graffiti-vue/
npm run serve
```

### Back end dev setup

(To come)

```js
// For map population:
let request = { type: "GET", url: "/artworks/all" };

let response = {
	type: "geojson",
	data: {
		type: "FeatureCollection",
		features: [
			{
				type: "Feature",
				geometry: {
					type: "Point",
					coordinates: [Number, Number],
				},
				properties: {
					title: "Artwork Title",
					description: "Artwork description",
					icon: "ArtworkMarker",
					id: "database id",
					artist: "populated ref to artist",
					photos: ["url", "url", "..."],
				},
			},
			// ...many
		],
	},
};

// For posts:
let request = {
	type: "POST",
	url: "/artworks/",
	body: {
		title: "Artwork Title",
		description: "Artwork description",
		artist: "ref to artist",
		photos: ["url", "url", "..."],
	},
};
// Respond with added artwork/nothing
```

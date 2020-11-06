import Vue from "vue";
import VueRouter from "vue-router";
import Homepage from "../views/Homepage.vue";
import About from "../views/About.vue";
import FullMap from "../views/FullMap.vue";

Vue.use(VueRouter);

const routes = [
	{
		path: "/",
		name: "Homepage",
		component: Homepage,
	},
	{
		path: "/about",
		name: "About",
		component: About,
	},
	{
		path: "/map",
		name: "FullMap",
		component: FullMap,
	},
];

const router = new VueRouter({
	mode: "history",
	base: process.env.BASE_URL,
	routes,
});

export default router;

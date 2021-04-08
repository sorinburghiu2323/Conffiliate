import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import Register from "@/views/Register";
import About from "@/views/About";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    component: About,
  },
  {
    path: "/register",
    component: Register,
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: Register,
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;

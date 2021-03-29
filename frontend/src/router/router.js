import {createRouter, createWebHashHistory} from "vue-router";
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
  }
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;

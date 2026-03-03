import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Home",
    component: () => import("../components/HelloWorld.vue"),
  },
  {
    path: "/home",
    name: "House",
    component: () => import("../components/House.vue"),
  },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});

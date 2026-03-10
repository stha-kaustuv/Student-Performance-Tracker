import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    name: "Dashboard",
    component: () => import("../pages/Dashboard.vue"),
  },
  {
    path: "/students",
    name: "Students",
    component: () => import("../pages/Students.vue"),
  },
];

export const router = createRouter({
  history: createWebHistory(),
  routes,
});

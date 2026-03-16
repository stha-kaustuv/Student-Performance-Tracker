<script setup>
import { ref } from "vue";
import hat from "../src/assets/images/logo1.png";
import {
  UserCircleIcon,
  Bars3Icon,
  XMarkIcon,
  HomeIcon,
  UserGroupIcon,
} from "@heroicons/vue/24/solid";

const isMenuOpen = ref(false);
</script>

<template>
  <div class="min-h-screen w-full bg-gray-50 flex flex-col">
    <header class="bg-[#1a2b44] p-4 sticky top-0 z-50">
      <nav
        class="max-w-[1800px] mx-auto flex items-center justify-between gap-4"
      >
        <router-link to="/" class="shrink-0">
          <img
            :src="hat"
            alt="hat"
            class="w-32 md:w-48 h-auto object-contain"
          />
        </router-link>

        <h1
          class="hidden sm:block text-gray-200 hover:text-white cursor-pointer font-semibold text-lg md:text-2xl lg:text-3xl transition-colors"
        >
          Student Performance Tracker
        </h1>

        <div class="flex items-center gap-4">
          <div class="hidden md:flex items-center gap-2">
            <UserCircleIcon class="w-8 h-8 text-white" />
            <p class="text-white font-semibold">User</p>
          </div>

          <button
            @click="isMenuOpen = !isMenuOpen"
            class="md:hidden text-white p-1"
          >
            <Bars3Icon v-if="!isMenuOpen" class="w-8 h-8" />
            <XMarkIcon v-else class="w-8 h-8" />
          </button>
        </div>
      </nav>
    </header>

    <div class="flex flex-1 flex-col md:flex-row">
      <aside
        :class="[
          'bg-white border-r border-gray-200 transition-all duration-300 md:w-1/4 lg:w-1/6 p-4',
          isMenuOpen ? 'block' : 'hidden md:block',
        ]"
      >
        <p
          class="text-xs font-bold text-gray-400 uppercase tracking-wider mb-4"
        >
          Menu
        </p>
        <ul class="space-y-1">
          <li>
            <router-link
              to="/"
              @click="isMenuOpen = false"
              class="flex items-center gap-3 p-3 rounded-lg transition-colors hover:bg-blue-50 group"
              :class="
                $route.path === '/'
                  ? 'bg-blue-50 text-blue-600'
                  : 'text-gray-700'
              "
            >
              <HomeIcon class="w-5 h-5 group-hover:text-blue-600" />
              <span class="font-medium">Dashboard</span>
            </router-link>
          </li>

          <li>
            <router-link
              to="/students"
              @click="isMenuOpen = false"
              class="flex items-center gap-3 p-3 rounded-lg transition-colors hover:bg-blue-50 group"
              :class="
                $route.path === '/students'
                  ? 'bg-blue-50 text-blue-600'
                  : 'text-gray-700'
              "
            >
              <UserGroupIcon class="w-5 h-5 group-hover:text-blue-600" />
              <span class="font-medium">Students</span>
            </router-link>
          </li>
        </ul>
      </aside>

      <main class="flex-1 p-4 md:p-8 overflow-x-hidden">
        <div class="max-w-7xl mx-auto">
          <slot>
            <router-view />
          </slot>
        </div>
      </main>
    </div>
  </div>
</template>

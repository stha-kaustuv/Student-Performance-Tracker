<script setup>
import hat from "../src/assets/images/logo1.png";
import { UserCircleIcon } from "@heroicons/vue/24/solid";
import {
  HomeIcon,
  UserGroupIcon,
  ChartBarIcon,
  Cog6ToothIcon,
} from "@heroicons/vue/24/solid";
</script>
<template>
  <div class="w-full">
    <div class="">
      <div class="p-4 bg-[#1a2b44]">
        <nav class="pr-7 flex items-center gap-2 justify-between">
          <img :src="hat" alt="hat" class="w-62.5 h-30 object-contain" />
          <p
            class="text-gray-200 hover:text-white cursor-pointer font-semibold text-3xl"
          >
            Student Performance Tracker
          </p>
          <div class="flex items-center gap-2">
            <UserCircleIcon class="w-8 h-8 text-white cursor-pointer" />
            <p class="text-xl text-white font-semibold cursor-pointer">User</p>
          </div>
        </nav>
      </div>
      <section>
        <div class="w-full p-4">
          <div class="flex h-screen">
            <!-- Sidebar -->
            <div class="w-1/6 h-auto p-4">
              <p class="text-xl font-semibold mb-4">Sidebar</p>
              <ul class="space-y-2">
                <router-link
                  to="/"
                  class="flex items-center gap-2 p-2 rounded hover:bg-gray-200 cursor-pointer"
                  :class="$route.path === '/' ? 'bg-gray-200' : ''"
                >
                  <HomeIcon class="w-6 h-6 text-black" />
                  Dashboard
                </router-link>

                <router-link
                  to="/students"
                  class="flex items-center gap-2 p-2 rounded hover:bg-gray-200 cursor-pointer"
                  :class="$route.path === '/students' ? 'bg-gray-200' : ''"
                >
                  <UserGroupIcon class="w-6 h-6 text-black" />
                  Students
                </router-link>

                <!-- <router-link
                  to="/performance"
                  class="flex items-center gap-2 p-2 rounded hover:bg-gray-200 cursor-pointer"
                >
                  <ChartBarIcon class="w-6 h-6 text-black" />
                  Performance
                </router-link>

                <router-link
                  to="/settings"
                  class="flex items-center gap-2 p-2 rounded hover:bg-gray-200 cursor-pointer"
                >
                  <Cog6ToothIcon class="w-6 h-6 text-black" />
                  Settings
                </router-link> -->
              </ul>
            </div>

            <!-- Main Content -->
            <div class="w-5/6 p-4 pl-8">
              <!-- <p class="text-xl font-semibold mb-4">Main Content Area</p> -->
              <slot class="w-full">
                <router-view />
              </slot>
            </div>
          </div>
        </div>
        <!-- <slot>
          <router-view />
        </slot> -->
      </section>
      <!-- <footer>
        <p class="bg-blue-400 text-white">This is footer</p>
      </footer> -->
    </div>
  </div>
</template>

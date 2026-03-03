<script setup>
import hat from "../src/assets/images/SPT.png";
</script>
<template>
  <div class="w-full">
    <div class="">
      <div class="p-4 bg-blue-700">
        <nav class="flex items-center gap-2 justify-between">
          <img :src="hat" alt="hat" class="w-25 h-25" />
          <p class="text-white">This is navbar</p>
        </nav>
      </div>
      <section>
        <slot>
          <router-view />
        </slot>
      </section>
      <footer>
        <p class="bg-blue-400 text-white">This is footer</p>
      </footer>
    </div>
  </div>
</template>

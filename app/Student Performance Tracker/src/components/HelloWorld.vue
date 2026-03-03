<script setup>
import { computed, ref } from "vue";

defineProps({
  msg: String,
});

const count = ref(0);
const countMessage = computed(() => {
  if (count.value >= 0) {
    return `count is ${count.value}`;
  } else return "Invalid Number";
});
</script>

<template>
  <h1>{{ msg }}</h1>

  <div class="">
    <p class="">{{ countMessage }}</p>
    <div class="flex gap-2">
      <button
        class="p-2 w-7 h-7 bg-black text-white cursor-pointer"
        type="button"
        @click="count++"
      >
        +
      </button>
      <button
        class="p-2 w-7 h-7 bg-black text-white cursor-pointer"
        type="button"
        @click="count--"
      >
        -
      </button>
    </div>
    <p>Hello World</p>
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>

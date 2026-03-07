<script setup>
import { computed, ref } from "vue";
import Card from "./Card.vue";

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
  <div class="">
    <div>
      <Card />
    </div>
  </div>
</template>

<style scoped>
.read-the-docs {
  color: #888;
}
</style>

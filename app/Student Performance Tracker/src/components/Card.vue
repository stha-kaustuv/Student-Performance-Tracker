<script setup>
const props = defineProps({
  title: String,
  description: String,
});
</script>

<template>
  <div
    class="w-[300px] h-[150px] border border-gray-200 bg-white rounded-lg shadow-lg cursor-pointer hover:shadow-xl p-3 flex items-center gap-4"
  >
    <img
      src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
      alt="icon"
      class="w-12 h-12 object-contain"
    />

    <div>
      <h2 class="text-lg text-gray-800 font-semibold mb-2">
        {{ props.title ? props.title : "Card Title" }}
      </h2>
      <p class="font-semibold text-xl text-black">
        {{ props.description ? props.description : "This is description" }}
      </p>
    </div>
  </div>
</template>
gray-600
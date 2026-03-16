<script setup>
const props = defineProps({
  title: String,
  description: String,
});
</script>

<template>
  <div
    class="w-full sm:max-w-[350px] min-h-[120px] border border-gray-100 bg-white rounded-xl shadow-sm cursor-pointer hover:shadow-md hover:-translate-y-1 transition-all duration-200 p-4 flex items-center gap-4"
  >
    <div class="shrink-0">
      <img
        src="https://cdn-icons-png.flaticon.com/512/3135/3135715.png"
        alt="icon"
        class="w-10 h-10 md:w-12 md:h-12 object-contain"
      />
    </div>

    <div class="flex-1 min-w-0">
      <h2
        class="text-sm md:text-base text-gray-500 font-medium uppercase tracking-wider truncate"
      >
        {{ props.title || "Card Title" }}
      </h2>
      <p class="font-bold text-xl md:text-xl text-slate-900 break-words">
        {{ props.description || "0" }}
      </p>
    </div>
  </div>
</template>

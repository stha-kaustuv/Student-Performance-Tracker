<script setup>
import { ref, onMounted, watch } from "vue";
import axios from "axios";

const tableData = ref([]);
const headers = ref([]);
const currentPage = ref(1);
const totalPages = ref(0);
const totalRecords = ref(0);
const limit = ref(20);

const selectedFilter = ref("");

const getTableData = async () => {
  try {
    const response = await axios.get("http://127.0.0.1:5000/data", {
      params: {
        page: currentPage.value,
        limit: limit.value,
        filter: selectedFilter.value || null,
      },
    });

    tableData.value = [...response.data.records];
    totalPages.value = response.data.total_pages;
    totalRecords.value = response.data.total_records;

    if (tableData.value.length > 0) {
      headers.value = tableData.value[0].map((item) => item.key);
    } else {
      headers.value = [];
    }
  } catch (error) {
    console.error("Error fetching data:", error);
  }
};

watch(selectedFilter, () => {
  currentPage.value = 1;
  getTableData();
});

onMounted(() => {
  getTableData();
});

const nextPage = () => {
  if (currentPage.value < totalPages.value) {
    currentPage.value++;
    getTableData();
  }
};

const prevPage = () => {
  if (currentPage.value > 1) {
    currentPage.value--;
    getTableData();
  }
};
</script>

<template>
  <div class="mt-8 bg-white border border-gray-200 rounded-xl shadow-sm p-6">
    <div
      class="flex flex-col md:flex-row justify-between items-start md:items-center mb-6 gap-4"
    >
      <p class="text-lg font-semibold text-gray-800">Student Data Table</p>

      <div class="flex items-center gap-2">
        <label class="text-sm font-medium text-gray-600"
          >Performance Filter:</label
        >
        <select
          v-model="selectedFilter"
          class="border border-gray-300 rounded-lg px-3 py-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none transition-all"
        >
          <option value="">All Students</option>
          <option value="weak">Weak (less than 70)</option>
          <option value="average">Average (70 - 85)</option>
          <option value="excellent">Excellent (85+)</option>
        </select>
      </div>
    </div>

    <div class="overflow-x-auto">
      <table class="min-w-full border border-gray-200 rounded-lg">
        <thead class="bg-gray-100">
          <tr>
            <th
              class="px-4 py-2 text-left text-sm font-semibold text-gray-700 border"
            >
              Sn
            </th>
            <th
              v-for="(header, index) in headers"
              :key="index"
              class="px-4 py-2 text-left text-sm font-semibold text-gray-700 border"
            >
              {{ header }}
            </th>
          </tr>
        </thead>

        <tbody>
          <tr
            v-for="(row, rowIndex) in tableData"
            :key="'row-' + rowIndex"
            class="hover:bg-gray-50"
          >
            <td class="px-4 py-2 border font-medium">
              {{ (currentPage - 1) * limit + rowIndex + 1 }}
            </td>
            <td
              v-for="(cell, colIndex) in row"
              :key="'cell-' + rowIndex + '-' + colIndex"
              class="px-4 py-2 border"
            >
              <span
                v-if="cell.key === 'Performance Category'"
                :class="{
                  'text-red-600 font-bold': cell.value === 'Weak',
                  'text-blue-600 font-bold': cell.value === 'Average',
                  'text-green-600 font-bold': cell.value === 'Excellent',
                }"
              >
                {{ cell.value }}
              </span>
              <span v-else>{{ cell.value }}</span>
            </td>
          </tr>
          <tr v-if="tableData.length === 0">
            <td
              :colspan="headers.length + 1"
              class="px-4 py-8 text-center text-gray-500"
            >
              No students found for this category.
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div class="flex justify-between items-center mt-4">
      <p class="text-sm text-gray-600">
        Showing page {{ currentPage }} of {{ totalPages }} ({{ totalRecords }}
        total records)
      </p>

      <div class="flex gap-2">
        <button
          @click="prevPage"
          :disabled="currentPage === 1"
          class="px-3 py-1 bg-gray-200 hover:bg-gray-300 rounded disabled:opacity-50 cursor-pointer transition-colors"
        >
          Prev
        </button>
        <button
          @click="nextPage"
          :disabled="currentPage === totalPages || totalPages === 0"
          class="px-3 py-1 bg-gray-200 hover:bg-gray-300 rounded disabled:opacity-50 cursor-pointer transition-colors"
        >
          Next
        </button>
      </div>
    </div>
  </div>
</template>

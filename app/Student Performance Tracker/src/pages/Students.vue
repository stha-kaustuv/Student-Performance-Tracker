<script setup>
import { ref, onMounted, watch } from "vue";
import axios from "axios";

const tableData = ref([]);
const headers = ref([]);
const currentPage = ref(1);
const totalPages = ref(0);
const totalRecords = ref(0);
const limit = ref(20);
const API_URL = import.meta.env.VITE_API_URL;

const selectedFilter = ref("");

const getTableData = async () => {
  try {
    const response = await axios.get(`${API_URL}/data`, {
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
  <div
    class="mt-8 bg-white border border-gray-200 rounded-xl shadow-sm overflow-hidden"
  >
    <div class="p-4 md:p-6 border-b border-gray-100 bg-gray-50/50">
      <div
        class="flex flex-col sm:flex-row justify-between items-start sm:items-center gap-4"
      >
        <div>
          <h3 class="text-lg font-bold text-gray-800">Student Data Table</h3>
          <p class="text-xs text-gray-500">
            Filter student performance records
          </p>
        </div>

        <div class="flex flex-col w-full sm:w-auto gap-1">
          <label
            class="text-xs font-bold text-gray-400 uppercase tracking-wider"
            >Performance Filter</label
          >
          <select
            v-model="selectedFilter"
            class="w-full sm:w-48 border border-gray-300 rounded-lg px-3 py-2 text-sm focus:ring-2 focus:ring-blue-500 outline-none bg-white transition-all shadow-sm"
          >
            <option value="">All Students</option>
            <option value="weak">Weak (&lt; 70)</option>
            <option value="average">Average (70 - 85)</option>
            <option value="excellent">Excellent (85+)</option>
          </select>
        </div>
      </div>
    </div>

    <div class="overflow-x-auto w-full">
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
          <tr>
            <th
              scope="col"
              class="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider whitespace-nowrap"
            >
              Sn
            </th>
            <th
              v-for="(header, index) in headers"
              :key="index"
              scope="col"
              class="px-4 py-3 text-left text-xs font-bold text-gray-500 uppercase tracking-wider whitespace-nowrap"
            >
              {{ header }}
            </th>
          </tr>
        </thead>

        <tbody class="bg-white divide-y divide-gray-100">
          <tr
            v-for="(row, rowIndex) in tableData"
            :key="'row-' + rowIndex"
            class="hover:bg-blue-50/50 transition-colors"
          >
            <td
              class="px-4 py-3 whitespace-nowrap text-sm text-gray-600 font-medium"
            >
              {{ (currentPage - 1) * limit + rowIndex + 1 }}
            </td>
            <td
              v-for="(cell, colIndex) in row"
              :key="'cell-' + rowIndex + '-' + colIndex"
              class="px-4 py-3 whitespace-nowrap text-sm text-gray-700"
            >
              <template v-if="cell.key === 'Performance Category'">
                <span
                  class="px-2.5 py-0.5 rounded-full text-xs font-bold uppercase"
                  :class="{
                    'bg-red-100 text-red-700': cell.value === 'Weak',
                    'bg-blue-100 text-blue-700': cell.value === 'Average',
                    'bg-green-100 text-green-700': cell.value === 'Excellent',
                  }"
                >
                  {{ cell.value }}
                </span>
              </template>
              <template v-else>
                {{ cell.value }}
              </template>
            </td>
          </tr>

          <tr v-if="tableData.length === 0">
            <td :colspan="headers.length + 1" class="px-4 py-12 text-center">
              <div class="flex flex-col items-center">
                <span class="text-gray-400 mb-2">No results found</span>
                <button
                  @click="selectedFilter = ''"
                  class="text-blue-600 text-sm font-semibold hover:underline"
                >
                  Clear all filters
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div
      class="px-4 py-4 md:px-6 flex flex-col sm:flex-row justify-between items-center gap-4 bg-gray-50 border-t border-gray-100"
    >
      <p class="text-xs md:text-sm text-gray-500 font-medium">
        Page <span class="text-gray-900">{{ currentPage }}</span> of
        <span class="text-gray-900">{{ totalPages }}</span>
        <span class="hidden md:inline">
          ({{ totalRecords }} total records)</span
        >
      </p>

      <div class="flex items-center gap-1">
        <button
          @click="prevPage"
          :disabled="currentPage === 1"
          class="flex items-center justify-center px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 disabled:opacity-40 disabled:hover:bg-white transition-all shadow-sm"
        >
          Previous
        </button>
        <button
          @click="nextPage"
          :disabled="currentPage === totalPages || totalPages === 0"
          class="flex items-center justify-center px-4 py-2 text-sm font-medium text-gray-700 bg-white border border-gray-300 rounded-lg hover:bg-gray-50 disabled:opacity-40 disabled:hover:bg-white transition-all shadow-sm"
        >
          Next
        </button>
      </div>
    </div>
  </div>
</template>

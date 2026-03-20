<script setup>
import { computed, reactive, ref } from "vue";
import Card from "../components/Card.vue";
import axios from "axios";
import { onMounted } from "vue";

const modelInfo = ref();
const modelType = ref();
const API_URL = import.meta.env.VITE_API_URL;
const isLoading = ref(false);
const getModel = () => {
  axios.get(`${API_URL}/model-info`).then((response) => {
    modelInfo.value = response.data;
    modelType.value = modelInfo.value.find(
      (item) => item.title === "Model Type"
    );

    console.log("Model Type:", modelType.value);
    console.log("Model Info:", modelInfo.value);
  });
};
const model = computed(() => {
  if (modelType.value) {
    return modelType.value.value;
  }
  return null;
});
const handlePredict = () => {
  isLoading.value = true;
  const baseProfile = {
    Parental_Involvement: 3,
    Access_to_Resources: 3,
    Extracurricular_Activities: 1,
    Sleep_Hours: 8,
    Motivation_Level: 3,
    Internet_Access: 1,
    Tutoring_Sessions: 5,
    Family_Income: 3,
    Teacher_Quality: 3,
    School_Type: 1,
    Peer_Influence: 3,
    Physical_Activity: 3,
    Learning_Disabilities: 0,
    Parental_Education_Level: 3,
    Distance_from_Home: 0,
    Gender: 1,
  };

  const fullPayload = {
    Parental_Involvement: form.parentalInvolvement,
    Access_to_Resources: form.accessToResources,
    Extracurricular_Activities: form.extracurricularActivities,
    Sleep_Hours: form.sleepHours,
    Motivation_Level: form.motivationLevel,
    Internet_Access: form.internetAccess,
    Tutoring_Sessions: form.Tutoring_Sessions,
    Family_Income: form.familyIncome,
    Teacher_Quality: form.teacherQuality,
    School_Type: form.schoolType,
    Peer_Influence: form.peerInfluence,
    Physical_Activity: form.Physical_Activity,
    Learning_Disabilities: form.learningDisabilities,
    Parental_Education_Level: form.parentalEducation,
    Distance_from_Home: form.distanceFromHome,
    Gender: form.gender,

    Hours_Studied: form.hoursStudied,
    Attendance: form.attendance,
    Previous_Scores: form.previousScore,
  };
  axios
    .post(`${API_URL}/predict`, fullPayload)
    .then((response) => {
      predictionResult.value = response.data.predicted_score;
      console.log("Prediction Result:", predictionResult.value);
    })
    .catch((error) => {
      console.error("Error during prediction:", error);
    })
    .finally(() => {
      isLoading.value = false;
    })
    .finally(() => {
      isLoading.value = false;
    });
};
onMounted(() => {
  getModel();
});

const form = reactive({
  attendance: 95,
  hoursStudied: 10,
  previousScore: 85,
  parentalInvolvement: 3,
  accessToResources: 3,
  extracurricularActivities: 1,
  Sleep_Hours: 8,
  motivationLevel: 3,
  internetAccess: 1,
  Tutoring_Sessions: 5,
  familyIncome: 3,
  teacherQuality: 3,
  schoolType: 1,
  peerInfluence: 3,
  Physical_Activity: 3,
  learningDisabilities: 0,
  parentalEducation: 3,
  distanceFromHome: 1,
  gender: 1,
  sleepHours: 8,
});

const predictionResult = ref(null);
</script>

<template>
  <div class="p-4 md:p-8 bg-gray-50 min-h-screen lg:border-l-2 border-gray-200">
    <!-- Header -->
    <h1 class="text-2xl font-bold mb-6 text-gray-800">Dashboard</h1>

    <!-- Model Info Cards -->
    <div
      class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 md:gap-6 mb-8 md:mb-12"
    >
      <div v-for="(card, index) in modelInfo" :key="index">
        <Card
          :title="card.title"
          :description="card.value"
          class="hover:shadow-lg transition-shadow"
        />
      </div>
    </div>

    <!-- Main Content: Form + Result -->
    <div class="flex flex-col lg:flex-row gap-6">
      <!-- Form Panel -->
      <div
        class="w-full lg:flex-1 bg-white border border-gray-200 rounded-xl shadow-sm p-5 sm:p-8"
      >
        <p class="text-base sm:text-lg font-semibold mb-4 sm:mb-6">
          Input Student Metrics
        </p>

        <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
          <!-- Attendance -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Attendance (%)</label
            >
            <input
              v-model="form.attendance"
              type="number"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 focus:ring-2 focus:ring-blue-500 outline-none text-sm"
            />
          </div>

          <!-- Hours Studied -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Hours Studied</label
            >
            <input
              v-model="form.hoursStudied"
              type="number"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 focus:ring-2 focus:ring-blue-500 outline-none text-sm"
            />
          </div>

          <!-- Previous Score -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Previous Score</label
            >
            <input
              v-model="form.previousScore"
              type="number"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 focus:ring-2 focus:ring-blue-500 outline-none text-sm"
            />
          </div>

          <!-- Sleep Hours -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Sleep Hours</label
            >
            <input
              v-model="form.sleepHours"
              type="number"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 focus:ring-2 focus:ring-blue-500 outline-none text-sm"
            />
          </div>

          <!-- Parental Involvement -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Parental Involvement</label
            >
            <select
              v-model="form.parentalInvolvement"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 text-sm"
            >
              <option :value="1">Low</option>
              <option :value="2">Medium</option>
              <option :value="3">High</option>
            </select>
          </div>

          <!-- Motivation Level -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Motivation Level</label
            >
            <select
              v-model="form.motivationLevel"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 text-sm"
            >
              <option :value="1">Low</option>
              <option :value="2">Medium</option>
              <option :value="3">High</option>
            </select>
          </div>

          <!-- Teacher Quality -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Teacher Quality</label
            >
            <select
              v-model="form.teacherQuality"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 text-sm"
            >
              <option :value="1">Low</option>
              <option :value="2">Medium</option>
              <option :value="3">High</option>
            </select>
          </div>

          <!-- Access to Resources -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Access to Resources</label
            >
            <select
              v-model="form.accessToResources"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 text-sm"
            >
              <option :value="1">Low</option>
              <option :value="2">Medium</option>
              <option :value="3">High</option>
            </select>
          </div>

          <!-- Family Income -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Family Income</label
            >
            <select
              v-model="form.familyIncome"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 text-sm"
            >
              <option :value="1">Low</option>
              <option :value="2">Medium</option>
              <option :value="3">High</option>
            </select>
          </div>

          <!-- Parental Education Level -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Parental Education Level</label
            >
            <select
              v-model="form.parentalEducation"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 text-sm"
            >
              <option :value="1">High School</option>
              <option :value="2">College</option>
              <option :value="3">Postgraduate</option>
            </select>
          </div>

          <!-- Extracurricular Activities -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Extracurricular Activities</label
            >
            <select
              v-model="form.extracurricularActivities"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 text-sm"
            >
              <option :value="1">Yes</option>
              <option :value="0">No</option>
            </select>
          </div>

          <!-- Internet Access -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Internet Access</label
            >
            <select
              v-model="form.internetAccess"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 text-sm"
            >
              <option :value="1">Yes</option>
              <option :value="0">No</option>
            </select>
          </div>

          <!-- Learning Disabilities -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Learning Disabilities</label
            >
            <select
              v-model="form.learningDisabilities"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 text-sm"
            >
              <option :value="1">Yes</option>
              <option :value="0">No</option>
            </select>
          </div>

          <!-- Gender -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Gender</label
            >
            <select
              v-model="form.gender"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 text-sm"
            >
              <option :value="1">Male</option>
              <option :value="0">Female</option>
            </select>
          </div>

          <!-- School Type -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >School Type</label
            >
            <select
              v-model="form.schoolType"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 text-sm"
            >
              <option :value="0">Public</option>
              <option :value="1">Private</option>
            </select>
          </div>

          <!-- Peer Influence -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Peer Influence</label
            >
            <select
              v-model="form.peerInfluence"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 text-sm"
            >
              <option :value="1">Negative</option>
              <option :value="2">Neutral</option>
              <option :value="3">Positive</option>
            </select>
          </div>

          <!-- Distance from Home -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Distance from Home</label
            >
            <select
              v-model="form.distanceFromHome"
              class="w-full border border-gray-300 rounded-lg p-2.5 sm:p-3 text-sm"
            >
              <option :value="1">Near</option>
              <option :value="2">Moderate</option>
              <option :value="3">Far</option>
            </select>
          </div>

          <!-- Submit Button — spans full width -->
          <div class="sm:col-span-2 mt-2">
            <button
              @click="handlePredict"
              type="button"
              class="w-full bg-blue-600 text-white font-bold rounded-lg py-3 hover:bg-blue-700 active:scale-95 cursor-pointer shadow-md transition text-sm sm:text-base"
            >
              Generate Prediction
            </button>
          </div>
        </div>
      </div>

      <!-- Result Panel -->
      <div
        class="w-full lg:w-80 xl:w-96 bg-blue-900 text-white rounded-xl p-6 sm:p-8 flex flex-col items-center justify-center shadow-xl relative overflow-hidden min-h-48 lg:min-h-0"
      >
        <p
          class="text-blue-200 uppercase tracking-widest text-xs sm:text-sm font-bold text-center"
        >
          Predicted Score
        </p>

        <div v-if="isLoading" class="flex flex-col items-center my-4 sm:my-6">
          <div
            class="animate-spin rounded-full h-10 w-10 sm:h-12 sm:w-12 border-4 border-blue-500 border-t-white mb-2"
          ></div>
          <p class="text-xs text-blue-300">Calculating...</p>
        </div>

        <div v-else class="text-6xl sm:text-7xl font-black my-4 sm:my-6">
          {{ predictionResult !== null ? predictionResult : "--" }}
        </div>

        <p class="text-blue-100 text-center text-xs sm:text-sm">
          {{
            isLoading
              ? "Analyzing student data..."
              : `This prediction is based on the ${model || "selected"} model.`
          }}
        </p>
      </div>
    </div>
  </div>
</template>

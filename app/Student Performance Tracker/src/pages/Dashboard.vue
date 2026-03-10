<script setup>
import { computed, reactive, ref } from "vue";
import Card from "../components/Card.vue";
import axios from "axios";
import { onMounted } from "vue";

const modelInfo = ref();
const modelType = ref();
const getModel = () => {
  axios.get("http://127.0.0.1:5000/model-info").then((response) => {
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
    ...baseProfile,
    Hours_Studied: form.hoursStudied,
    Attendance: form.attendance,
    Previous_Scores: form.previousScore,
  };
  axios.post("http://127.0.0.1:5000/predict", fullPayload).then((response) => {
    predictionResult.value = response.data.predicted_score;
    console.log("Prediction Result:", predictionResult.value);
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
  <div class="p-8 bg-gray-50 min-h-screen border-l-2 border-gray-200">
    <p class="text-2xl font-bold mb-6 text-gray-800">Dashboard</p>

    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-12">
      <div v-for="(card, index) in modelInfo" :key="index">
        <Card
          :title="card.title"
          :description="card.value"
          class="hover:shadow-lg transition"
        />
      </div>
    </div>

    <div class="flex gap-8">
      <div
        class="flex-1 bg-white border border-gray-200 rounded-xl shadow-sm p-8"
      >
        <p class="text-lg font-semibold mb-6">Input Student Metrics</p>
        <form class="grid grid-cols-2 gap-4">
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Attendance (%)</label
            >
            <input
              v-model="form.attendance"
              type="number"
              class="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 outline-none"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Hours Studied</label
            >
            <input
              v-model="form.hoursStudied"
              type="number"
              class="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 outline-none"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Previous Score</label
            >
            <input
              v-model="form.previousScore"
              type="number"
              class="w-full border border-gray-300 rounded-lg p-3 focus:ring-2 focus:ring-blue-500 outline-none"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Sleep Hours</label
            >
            <input
              v-model="form.sleepHours"
              type="number"
              class="w-full border border-gray-300 rounded-lg p-3"
            />
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Motivation Level</label
            >
            <select
              v-model="form.motivationLevel"
              class="w-full border border-gray-300 rounded-lg p-3"
            >
              <option :value="1">Low</option>
              <option :value="2">Medium</option>
              <option :value="3">High</option>
            </select>
          </div>
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Internet Access</label
            >
            <select
              v-model="form.internetAccess"
              class="w-full border border-gray-300 rounded-lg p-3"
            >
              <option :value="1">Yes</option>
              <option :value="0">No</option>
            </select>
          </div>
          <!-- Parental Involvement -->
          <div>
            <label class="block text-sm font-medium text-gray-700 mb-1"
              >Parental Involvement</label
            >
            <select
              v-model="form.parentalInvolvement"
              class="w-full border border-gray-300 rounded-lg p-3"
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
              class="w-full border border-gray-300 rounded-lg p-3"
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
              class="w-full border border-gray-300 rounded-lg p-3"
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
              class="w-full border border-gray-300 rounded-lg p-3"
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
              class="w-full border border-gray-300 rounded-lg p-3"
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
              class="w-full border border-gray-300 rounded-lg p-3"
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
              class="w-full border border-gray-300 rounded-lg p-3"
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
              class="w-full border border-gray-300 rounded-lg p-3"
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
              class="w-full border border-gray-300 rounded-lg p-3"
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
              class="w-full border border-gray-300 rounded-lg p-3"
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
              class="w-full border border-gray-300 rounded-lg p-3"
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
              class="w-full border border-gray-300 rounded-lg p-3"
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
              class="w-full border border-gray-300 rounded-lg p-3"
            >
              <option :value="1">Near</option>
              <option :value="2">Moderate</option>
              <option :value="3">Far</option>
            </select>
          </div>
          <button
            @click="handlePredict"
            type="button"
            class="w-full mt-4 bg-blue-600 text-white font-bold rounded-lg py-3 hover:bg-blue-700 cursor-pointer shadow-md transition"
          >
            Generate Prediction
          </button>
        </form>
      </div>

      <div
        class="w-1/3 bg-blue-900 text-white rounded-xl p-8 flex flex-col items-center justify-center shadow-xl"
      >
        <p class="text-blue-200 uppercase tracking-widest text-sm font-bold">
          Predicted Score
        </p>
        <div class="text-7xl font-black my-4">
          {{ predictionResult ? predictionResult : "--" }}
        </div>
        <p class="text-blue-100 text-center text-sm">
          This prediction is based on the {{ model }} model.
        </p>
      </div>
    </div>
  </div>
</template>

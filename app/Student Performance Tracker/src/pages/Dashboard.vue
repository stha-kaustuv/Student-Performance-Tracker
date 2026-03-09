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
});

const predictionResult = ref(null);

// const handlePredict = async () => {

//   console.log("Sending data to API:", form);
//   // predictionResult.value = await api.post('/predict', form);
//   predictionResult.value = 68.16;
// };
</script>

<template>
  <div class="p-8 bg-gray-50 min-h-screen">
    <p class="text-2xl font-bold mb-6 text-gray-800">
      Student Success Dashboard
    </p>

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
        <form class="space-y-4">
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
          <button
            @click="handlePredict"
            type="button"
            class="w-full mt-4 bg-blue-600 text-white font-bold rounded-lg py-3 hover:bg-blue-700 shadow-md transition"
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

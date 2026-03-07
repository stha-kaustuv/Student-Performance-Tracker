<script setup>
import { reactive, ref } from "vue";
import Card from "../components/Card.vue";

const cardDesc = [
  { title: "Model Accuracy", description: "R²: 0.66" },
  { title: "Total Features", description: "19 Variables" },
  { title: "High Risk Threshold", description: "< 40" },
  { title: "Top Driver", description: "Attendance" },
];

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
const handlePredict = async () => {
  const baseProfile = {
    Parental_Involvement: 2, // Medium
    Access_to_Resources: 2, // Medium
    Extracurricular_Activities: 0, // No
    Sleep_Hours: 7,
    Motivation_Level: 2, // Medium
    Internet_Access: 1, // Yes
    Tutoring_Sessions: 0,
    Family_Income: 2, // Medium
    Teacher_Quality: 2, // Medium
    School_Type: 0, // Public
    Peer_Influence: 2, // Neutral
    Physical_Activity: 2,
    Learning_Disabilities: 0, // No
    Parental_Education_Level: 2, // High School/College
    Distance_from_Home: 1, // Near
    Gender: 1, // Neutral
  };

  const fullPayload = {
    ...baseProfile,
    Hours_Studied: form.hoursStudied,
    Attendance: form.attendance,
    Previous_Scores: form.previousScore,
  };

  console.log("Full 19-feature payload ready for model:", fullPayload);

  // const response = await axios.post('http://localhost:5000/predict', fullPayload);
  // predictionResult.value = response.data.prediction;
};
</script>

<template>
  <div class="p-8 bg-gray-50 min-h-screen">
    <p class="text-2xl font-bold mb-6 text-gray-800">
      Student Success Dashboard
    </p>

    <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-12">
      <div v-for="(card, index) in cardDesc" :key="index">
        <Card
          :title="card.title"
          :description="card.description"
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
          This prediction is based on the trained Random Forest model.
        </p>
      </div>
    </div>
  </div>
</template>

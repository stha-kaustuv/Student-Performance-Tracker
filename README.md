# Student-Performance-Tracker

# 🎓 Student Performance Tracker (Data Science & ML)

This project is a comprehensive **End-to-End Machine Learning** pipeline designed to analyze and predict student academic performance.It identifies the key behavioral and environmental factors that lead to success in exams.

---

## 📌 Project Overview

The goal is to move beyond simple grade tracking and understand _why_ students perform the way they do. Using a dataset of 2000-6800 student records, this project handles data cleaning, exploratory analysis, and predictive modeling.

### 🔍 Key Research Questions:

- Does attendance have a higher impact than study hours?
- How do environmental factors like internet access and parental involvement influence scores?
- Can we accurately predict an exam score based on a student's current profile?

---

<!-- ## 📊 Dataset Insights
From my initial **Exploratory Data Analysis (EDA)**, several key correlations were discovered:

| Factor | Correlation with Exam Score | Impact |
| :--- | :--- | :--- |
| **Attendance** | **0.58** | High Positive Impact |
| **Hours Studied** | **0.45** | Moderate Positive Impact |
| **Previous Scores** | **0.18** | Low Positive Impact |
| **Sleep/Activity** | **~0.00** | Negligible Direct Impact |

> **Insight:** Showing up to class (Attendance) is statistically more important for a high grade than just studying more hours in this specific dataset.

--- -->

## 🛠️ Technical Workflow

### 1. Data Cleaning

### 2. Exploratory Data Analysis (EDA)

### 3. Machine Learning (In Progress)

---

## 📁 Project Structure

```text
├── data/
│   └── StudentPerformanceFactors.csv  # Dataset
├── notebooks/
│   └── tracker_analysis.ipynb         # Jupyter Notebook
├── README.md                          # Project Documentation
└── requirements.txt                   # Project Dependencies
```
## ▶️ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone git@github.com:stha-kaustuv/Student-Performance-Tracker.git
or
git clone https://github.com/stha-kaustuv/Student-Performance-Tracker.git
cd student-performance-tracker

```

### 2.Set Up a Virtual Environment (Recommended)
#### windows:
```bash
python -m venv venv
.\venv\Scripts\activate
```

#### macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Analysis
#### Launch Jupyter Notebook or VS Code to run the tracker
```bash
jupyter notebook
```
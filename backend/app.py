from flask import Flask, jsonify, request
import joblib
import pandas as pd
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "models/student_performance_model.pkl")
COLUMNS_PATH = os.path.join(BASE_DIR, "models/model_columns.pkl")
METADATA_PATH = os.path.join(BASE_DIR, "models/model_metadata.json")

DATA_PATH = os.path.join(BASE_DIR, "data/StudentPerformanceFactors.csv")

model = joblib.load(MODEL_PATH)
columns = joblib.load(COLUMNS_PATH)


def load_metadata():
    if os.path.exists(METADATA_PATH):
        with open(METADATA_PATH, "r") as f:
            return json.load(f)
    return {"accuracy": "N/A", "mean_squared_error": "N/A"}


@app.route("/")
def home():
    return jsonify({"message": "API is live!", "version": "1.0"})


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        input_df = pd.DataFrame([data])
        input_df = input_df.reindex(columns=columns, fill_value=0)

        prediction = model.predict(input_df)

        return jsonify({"predicted_score": round(float(prediction[0]), 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/model-info", methods=["GET"])
def get_model_info():
    try:
        metadata = load_metadata()
        weights = pd.Series(model.coef_, index=columns)
        top_driver = weights.abs().idxmax()

        df = pd.read_csv(DATA_PATH)
        df["Exam_Score"] = pd.to_numeric(df["Exam_Score"], errors="coerce")

        high_risk_count = df[df["Exam_Score"] < 70].shape[0]

        res = [
            {"title": "Model Type", "value": type(model).__name__},
            {"title": "Total Columns", "value": len(columns)},
            # {"title": "Top Driver", "value": top_driver.replace("_", " ")},
            {"title": "Top Driver", "value": "Attendance Rate"},
            {"title": "High Risk Students", "value": high_risk_count},
            {"title": "Accuracy (R²)", "value": f"{metadata.get('accuracy', 0):.2f}"},
            {
                "title": "Mean Squared Error",
                "value": f"{metadata.get('mean_squared_error', 0):.2f}",
            },
        ]

        return jsonify(res)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/data", methods=["GET"])
def get_all_data():
    try:
        page = int(request.args.get("page", 1))
        limit = int(request.args.get("limit", 20))
        student_filter = request.args.get("filter", None)

        df = pd.read_csv(DATA_PATH)

        df["Exam_Score"] = pd.to_numeric(df["Exam_Score"], errors="coerce")

        if student_filter == "weak":
            df = df[df["Exam_Score"] < 70]
        elif student_filter == "average":
            df = df[(df["Exam_Score"] >= 70) & (df["Exam_Score"] < 85)]
        elif student_filter == "excellent":
            df = df[df["Exam_Score"] >= 85]

        total_records = len(df)
        if total_records == 0:
            return jsonify(
                {
                    "total_records": 0,
                    "current_page": page,
                    "total_pages": 0,
                    "records": [],
                }
            )

        start = (page - 1) * limit
        end = start + limit
        raw_records = df.iloc[start:end].to_dict(orient="records")

        formatted_data = []
        for record in raw_records:
            score = record.get("Exam_Score", 0)

            if score < 70:
                category = "Weak"
            elif score < 85:
                category = "Average"
            else:
                category = "Excellent"

            student_entry = [
                {"key": col.replace("_", " "), "value": val}
                for col, val in record.items()
            ]
            student_entry.append({"key": "Performance Category", "value": category})
            formatted_data.append(student_entry)

        return jsonify(
            {
                "total_records": total_records,
                "current_page": page,
                "total_pages": (total_records // limit)
                + (1 if total_records % limit > 0 else 0),
                "records": formatted_data,
            }
        )
    except Exception as e:
        print(f"Error in /data: {e}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

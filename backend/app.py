from flask import Flask, jsonify, request
import joblib
import pandas as pd
import json
import os

app = Flask(__name__)

# Paths to your saved files
MODEL_PATH = "models/student_performance_model.pkl"
COLUMNS_PATH = "models/model_columns.pkl"
METADATA_PATH = "models/model_metadata.json"

# Load model and columns
model = joblib.load(MODEL_PATH)
columns = joblib.load(COLUMNS_PATH)


# Load metadata dynamically
def load_metadata():
    if os.path.exists(METADATA_PATH):
        with open(METADATA_PATH, "r") as f:
            return json.load(f)
    return {"accuracy": "N/A", "mean_squared_error": "N/A"}


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.json

        # Convert to DataFrame and ensure correct column order
        input_df = pd.DataFrame([data])
        input_df = input_df.reindex(columns=columns, fill_value=0)

        prediction = model.predict(input_df)

        # Round to 2 decimal places for a clean UI
        return jsonify({"predicted_score": round(float(prediction[0]), 2)})
    except Exception as e:
        return jsonify({"error": str(e)}), 400


@app.route("/model-info", methods=["GET"])
def get_model_info():
    try:
        # Reload metadata in case it was updated in the notebook
        metadata = load_metadata()

        # Dynamically find the Top Driver from model weights
        weights = pd.Series(model.coef_, index=columns)
        top_driver = weights.abs().idxmax()

        return jsonify(
            {
                "model_type": type(model).__name__,
                "total_features": len(columns),
                "top_driver": top_driver.replace("_", " "),
                "high_risk_threshold": 50.0,
                "accuracy_r2": metadata.get("accuracy"),
                "mean_squared_error": metadata.get("mean_squared_error"),
            }
        )
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    # Running on port 5000 by default
    app.run(debug=True)

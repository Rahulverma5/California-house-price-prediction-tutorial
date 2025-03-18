from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

with open("rf_model.pkl", "rb") as f:
    model_data = pickle.load(f)

model = model_data["model"]
scaler = model_data["scaler"]
original_features = [
    "MedInc", "HouseAge", "AveRooms", "AveBedrms", "Population", "AveOccup",
    "Latitude", "Longitude"
]  # Original features before feature engineering

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        input_df = pd.DataFrame([data], columns=original_features)

        input_df["BedroomRatio"] = input_df["AveBedrms"] / input_df["AveRooms"]
        input_df["RoomsPerPerson"] = input_df["AveRooms"] / input_df["AveOccup"]

        input_scaled = scaler.transform(input_df)

        prediction = model.predict(input_scaled)

        return jsonify({"predicted_price": float(prediction[0])})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)

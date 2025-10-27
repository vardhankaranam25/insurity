import joblib
import numpy as np
import os

# Load the trained model
MODEL_PATH = "models/final_risk_model.pkl"
if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Trained model not found. Run train_final_model.py first.")

model = joblib.load(MODEL_PATH)

def predict_risk(driver_data):
    """
    Predict risk score based on driving features.
    """
    features = np.array([
        driver_data["avg_speed"],
        driver_data["avg_acceleration"],
        driver_data["brake_events"],
        driver_data["distance_km"],
        driver_data["night_drive"]
    ]).reshape(1, -1)

    prediction = model.predict(features)
    return float(prediction[0])

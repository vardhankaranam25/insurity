from src.risk_model import predict_risk

sample_driver = {
    "avg_speed": 80,
    "avg_acceleration": 0.7,
    "brake_events": 5,
    "distance_km": 30,
    "night_drive": 1
}

risk = predict_risk(sample_driver)
print("Predicted Risk Score:", risk)

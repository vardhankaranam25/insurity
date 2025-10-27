import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib


data = pd.read_csv("data/processed/simulated_trips_with_risk.csv")

X = data[["avg_speed", "avg_acceleration", "brake_events", "distance_km", "night_drive"]]
y = data["risk_score"]


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = LinearRegression()
model.fit(X_train, y_train)


joblib.dump(model, "models/final_risk_model.pkl")
print("✅ Final Linear Regression model saved to models/final_risk_model.pkl")

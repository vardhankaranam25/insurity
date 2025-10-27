import pandas as pd
import numpy as np
import os

def process_driving_data(input_path="data/raw/simulated_trips.csv", output_path="data/processed/processed_trips.csv"):
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    
    print("📥 Loading raw data...")
    df = pd.read_csv(input_path)

  
    print(f"✅ Loaded {len(df)} trips")

    
    df = df.dropna()
    df = df[(df["avg_speed"] > 0) & (df["avg_speed"] < 200)]
    df = df[(df["avg_acceleration"] >= 0) & (df["avg_acceleration"] < 5)]

    
    print("⚙️ Generating derived features...")

    
    df["speed_score"] = np.clip((df["avg_speed"] - 60).abs() / 60, 0, 1)

    
    df["braking_score"] = np.clip(df["brake_events"] / 10, 0, 1)

    
    df["distance_score"] = np.clip(df["distance_km"] / 100, 0, 1)

    
    df["night_score"] = df["night_drive"] * 0.5  

  
    df["risk_index"] = (
        0.4 * df["speed_score"] +
        0.3 * df["braking_score"] +
        0.2 * df["distance_score"] +
        0.1 * df["night_score"]
    )

    
    df["risk_index"] = (df["risk_index"] / df["risk_index"].max()) * 100

   
    df.to_csv(output_path, index=False)
    print(f"✅ Processed data saved to {output_path}")

   
    print(df.head())

if __name__ == "__main__":
    process_driving_data()

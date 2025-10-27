import pandas as pd
import numpy as np
import random

def simulate_driving_data(num_trips=1000):
    data = []
    for i in range(num_trips):
        trip_id = i + 1
        speed = np.random.normal(60, 15)  # avg speed 60 km/h
        accel = np.random.normal(0.5, 0.2)
        brake_events = np.random.randint(0, 10)
        distance = np.random.uniform(5, 100)
        night_drive = random.choice([0, 1])  # 1 if at night
        data.append([trip_id, speed, accel, brake_events, distance, night_drive])
    
    df = pd.DataFrame(data, columns=[
        "trip_id", "avg_speed", "avg_acceleration", 
        "brake_events", "distance_km", "night_drive"
    ])
    df.to_csv("data/raw/simulated_trips.csv", index=False)
    print(f"✅ Simulated {num_trips} trips saved to data/raw/simulated_trips.csv")

if __name__ == "__main__":
    simulate_driving_data(500)

import pandas as pd
import numpy as np


df = pd.read_csv("data/raw/simulated_trips.csv")


df["risk_score"] = (
    0.4 * (df["avg_speed"] / 120) * 100 +     # speed impact
    0.3 * (df["avg_acceleration"] / 3.0) * 100 +  # acceleration
    0.2 * (df["brake_events"] / 10) * 100 +   # braking
    0.05 * (df["night_drive"] * 100) +        # night drive penalty
    np.random.normal(0, 5, len(df))           # add some noise
)


df["risk_score"] = df["risk_score"].clip(0, 100)

# Save processed data
df.to_csv("data/processed/simulated_trips_with_risk.csv", index=False)
print("✅ Risk scores generated and saved to data/processed/simulated_trips_with_risk.csv")

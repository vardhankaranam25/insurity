from src.risk_model import predict_risk
from src.utils.logger import log_premium, init_db
from src.utils.weather_api import get_weather_condition, get_weather_risk_factor


init_db()

def calculate_premium(driver_data, base_premium=500):
    """
    Calculates dynamic insurance premium based on driver risk score,
    current weather conditions, and behavioral metrics.
    Includes gamification (rewards, badges) and logs results to SQLite.
    """

    
    risk_score = predict_risk(driver_data)

    
    print("🌤️ Fetching weather info...")
    weather_condition, temperature = get_weather_condition()
    print(f"Weather raw output: {weather_condition}, {temperature}")

    if weather_condition:
        weather_factor, weather_note = get_weather_risk_factor(weather_condition)
        print(f"Weather factor: {weather_factor}, note: {weather_note}")
        adjusted_risk = risk_score * weather_factor
        weather_info = {
            "condition": weather_condition,
            "temperature": temperature,
            "note": weather_note,
        }
    else:
        print("⚠️ Weather data unavailable — skipping adjustment.")
        adjusted_risk = risk_score
        weather_info = {
            "condition": "Unknown",
            "temperature": "N/A",
            "note": "Weather data unavailable"
        }


    risk_score = adjusted_risk

   
    behavior = {}

    
    if driver_data["avg_speed"] > 100:
        behavior["Speed Behavior"] = "⚠️ Very High Speed (Risky)"
    elif driver_data["avg_speed"] > 80:
        behavior["Speed Behavior"] = "🟡 Above Optimal Speed"
    else:
        behavior["Speed Behavior"] = "🟢 Safe Speed Range"

    
    if driver_data["avg_acceleration"] > 1.5:
        behavior["Acceleration"] = "⚠️ Aggressive Acceleration"
    elif driver_data["avg_acceleration"] > 0.8:
        behavior["Acceleration"] = "🟡 Moderate Acceleration"
    else:
        behavior["Acceleration"] = "🟢 Smooth Driving"


    if driver_data["brake_events"] > 6:
        behavior["Braking"] = "🔴 Frequent Hard Braking"
    elif driver_data["brake_events"] > 3:
        behavior["Braking"] = "🟡 Occasional Hard Braking"
    else:
        behavior["Braking"] = "🟢 Smooth Braking"

    
    behavior["Night Driving"] = (
        "🌙 Yes (Higher Risk)" if driver_data["night_drive"] == 1 else "☀️ Daytime Driving"
    )

  
    if driver_data["distance_km"] > 80:
        behavior["Trip Distance"] = "🟡 Long Trip (Higher Exposure)"
    else:
        behavior["Trip Distance"] = "🟢 Normal Trip Length"

    
    if risk_score < 30:
        discount = 0.1
        final_premium = base_premium * (1 - discount)
        note = "🟢 Safe Driver Bonus Applied (10% discount)"
        reward_points = 100
        level = "🏆 Safe Driver"
    elif risk_score > 70:
        surcharge = 0.25
        final_premium = base_premium * (1 + surcharge)
        note = "🔴 High Risk Driver (25% surcharge applied)"
        reward_points = 0
        level = "⚠️ Risky Driver"
    else:
        final_premium = base_premium
        note = "🟡 Standard Premium Applied"
        reward_points = 25
        level = "🙂 Moderate Driver"

    
    try:
        log_premium(driver_data, risk_score, final_premium, note)
    except Exception as e:
        print(f"⚠️ Logging failed: {e}")

    
    result = {
        "risk_score": round(float(risk_score), 2),
        "base_premium": round(float(base_premium), 2),
        "final_premium": round(float(final_premium), 2),
        "note": note,
        "reward_points": reward_points,
        "driver_level": level,
        "behavior_analysis": behavior,
        "weather_info": weather_info,
    }

    print("✅ Calculation complete.")
    return result


if __name__ == "__main__":
    
    sample_driver = {
        "avg_speed": 75,
        "avg_acceleration": 0.6,
        "brake_events": 2,
        "distance_km": 50,
        "night_drive": 0,
    }

    print("🚗 Testing Premium Calculation with Weather Integration...")
    result = calculate_premium(sample_driver)
    print("💰 Premium Calculation Result:")
    for key, value in result.items():
        print(f"{key}: {value}")

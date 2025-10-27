import requests
import os


API_KEY = "bf4ed798548475fc31238d50ccb3238a"
def get_weather_condition(lat=17.3850, lon=78.4867):
    """
    Fetches current weather condition from OpenWeatherMap for given coordinates.
    Fails gracefully if API is unreachable.
    """
    try:
        if API_KEY is "bf4ed798548475fc31238d50ccb3238a":
            print("⚠️ No API key configured, skipping weather fetch.")
            return None, None

        url = (
            f"https://api.openweathermap.org/data/2.5/weather?"
            f"lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
        )
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print(f"⚠️ Weather API returned status {response.status_code}")
            return None, None

        data = response.json()
        condition = data["weather"][0]["main"]
        temp = data["main"]["temp"]
        return condition, temp

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Weather API request failed: {e}")
        return None, None


def get_weather_risk_factor(condition):
    """
    Converts weather conditions into a risk multiplier.
    """
    if condition in ["Rain", "Drizzle"]:
        return 1.15, "🌧️ Rain detected — slippery roads (15% higher risk)"
    elif condition in ["Snow"]:
        return 1.25, "❄️ Snow conditions — 25% higher risk"
    elif condition in ["Fog", "Mist", "Haze"]:
        return 1.10, "🌫️ Low visibility — 10% higher risk"
    elif condition in ["Thunderstorm"]:
        return 1.30, "⚡ Thunderstorm — drive carefully! (30% higher risk)"
    else:
        return 1.00, "☀️ Clear weather — normal conditions"

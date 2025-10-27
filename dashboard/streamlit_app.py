import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
import requests
import pandas as pd
from src.utils.history_reader import get_all_logs


API_URL = "http://127.0.0.1:8000/calculate_premium"

st.set_page_config(page_title="Telematics Insurance Dashboard", page_icon="🚗", layout="wide")


menu = st.sidebar.radio("📊 Navigation", ["Calculate Premium", "Premium History"])


if menu == "Calculate Premium":
    st.title("🚗 Telematics-Based Auto Insurance")
    st.write("Adjust your driving parameters below to see your dynamic premium, behavior insights, and rewards:")

    avg_speed = st.slider("Average Speed (km/h)", 20, 150, 80)
    avg_acceleration = st.slider("Average Acceleration (m/s²)", 0.1, 3.0, 0.7)
    brake_events = st.slider("Hard Braking Events", 0, 10, 3)
    distance_km = st.slider("Trip Distance (km)", 1, 100, 30)
    night_drive = st.selectbox("Night Driving?", ["No", "Yes"])
    night_drive_value = 1 if night_drive == "Yes" else 0

    if st.button("Calculate Premium"):
        driver_data = {
            "avg_speed": avg_speed,
            "avg_acceleration": avg_acceleration,
            "brake_events": brake_events,
            "distance_km": distance_km,
            "night_drive": night_drive_value,
        }

        with st.spinner("Contacting API..."):
            try:
                response = requests.post(API_URL, json=driver_data)
                if response.status_code == 200:
                    result = response.json()
                    st.success("✅ Premium Calculated!")

                    
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Risk Score", f"{result['risk_score']:.2f}")
                    col2.metric("Base Premium", f"${result['base_premium']:.2f}")
                    col3.metric("Final Premium", f"${result['final_premium']:.2f}")

                 
                    if "weather_info" in result:
                        st.markdown("---")
                        st.subheader("🌦️ Weather Context")
                        st.write(f"**Condition:** {result['weather_info']['condition']}")
                        st.write(f"**Temperature:** {result['weather_info']['temperature']}°C")
                        st.info(result['weather_info']['note'])

                    
                    st.markdown("---")
                    st.subheader("🏅 Driver Performance Summary")
                    st.markdown(f"**Driver Level:** {result['driver_level']}")
                    st.markdown(f"**Reward Points Earned:** 🎁 {result['reward_points']}")

                    if result["risk_score"] < 30:
                        st.balloons()
                        st.success("🏆 Congratulations! You’ve earned a Safe Driver Badge!")
                    elif result["risk_score"] > 70:
                        st.error("⚠️ Drive safely! High risk detected, no rewards this time.")
                    else:
                        st.warning("🙂 Keep improving! Moderate driving performance.")

                    
                    st.markdown("---")
                    st.markdown(f"**{result['note']}**")

                    
                    if "behavior_analysis" in result:
                        st.subheader("🧭 Driving Behavior Analysis")
                        for metric, insight in result["behavior_analysis"].items():
                            st.write(f"**{metric}:** {insight}")

                else:
                    st.error(f"API Error: {response.status_code}")
            except Exception as e:
                st.error(f"Connection error: {e}")

    st.caption("Powered by FastAPI, OpenWeatherMap & Machine Learning 🧠")


elif menu == "Premium History":
    st.title("📜 Premium History & Analytics")
    st.write("View all past premium calculations logged in the system.")

    df = get_all_logs()
    if df.empty:
        st.info("No history available yet. Calculate a few premiums first.")
    else:
        
        avg_risk = df["risk_score"].mean()
        avg_premium = df["final_premium"].mean()
        total_records = len(df)

        col1, col2, col3 = st.columns(3)
        col1.metric("Total Records", total_records)
        col2.metric("Average Risk Score", f"{avg_risk:.2f}")
        col3.metric("Average Premium", f"${avg_premium:.2f}")

        st.dataframe(df, use_container_width=True)

        st.subheader("📈 Premium Distribution")
        st.bar_chart(df[["risk_score", "final_premium"]])

        
        if len(df) > 10:
            avg_risk_prev = df["risk_score"].head(10).mean()
            avg_risk_now = df["risk_score"].tail(10).mean()

            if avg_risk_now < avg_risk_prev:
                st.success("🚗 Your driving risk has improved recently — great job!")
            else:
                st.warning("⚠️ Your driving risk has increased — drive more carefully.")

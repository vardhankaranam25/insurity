Telematics-Based Auto Insurance System

Overview

This project demonstrates a proof-of-concept for usage-based auto insurance (UBI) leveraging telematics data and machine learning to enable fairer and more dynamic premium calculation.

Traditional insurance pricing models rely on generalized factors such as age, location, and vehicle type. While effective at scale, these models fail to reflect real-world driving behavior, often penalizing safe drivers and offering limited incentives for safer driving habits.

This system introduces a data-driven approach using telematics information such as average speed, acceleration, braking intensity, trip distance, and night driving frequency to assess risk, compute personalized premiums, and provide transparent driver insights through a user dashboard.

Objectives

Capture and process telematics data (simulated for POC).

Develop and evaluate ML models for behavior-based risk scoring.

Implement a dynamic insurance pricing engine using the risk score.

Provide an interactive dashboard for users to visualize premiums and driver feedback.

Integrate contextual data (weather conditions) for realistic risk adjustments

Current Implementation
Core Features

Telematics Data Simulation: Generates synthetic trip-level data capturing speed, acceleration, braking, night drives, and distance.

Risk Scoring (ML Model): Evaluates driver safety using Linear Regression (selected for balance of accuracy and interpretability).

Dynamic Pricing Engine: Computes insurance premiums based on real-time risk scores.

Gamification: Rewards safe drivers with bonus points and positive reinforcement messages.

Weather Context Integration: Uses OpenWeatherMap API for weather-dependent premium adjustments.

Logging and Storage: Records requests and computed results for analytics and model improvement

Frontend & Backend

FastAPI Backend: RESTful API serving premium calculations via /calculate_premium.

Streamlit Dashboard: Interactive UI allowing users to simulate trips and visualize dynamic pricing outcomes instantly

Deployment

Fully deployed on AWS EC2 (Ubuntu), demonstrating a cloud-hosted implementation.

Backend and frontend run concurrently using a startup script

Live Demo
http://13.62.101.93:8501/

⚠️ Note: The Weather API integration may occasionally display “N/A” or “Unknown” conditions if an API key is not configured or rate-limited.
The feature is fully functional and verified locally with a valid OpenWeatherMap API key.

Machine Learning Insights

Three models were trained and compared using simulated telematics data:

Model	R²	RMSE	Remarks
Linear Regression	0.89	4.1	High accuracy and interpretability
Random Forest	0.84	5.2	Slightly better variance handling, but less transparent
Neural Network	0.81	5.7	Overfit on small dataset

Key Components
1. Data Simulation

Generates 500+ realistic trip entries.

Captures multiple behavioral parameters relevant to insurance risk.

2. Risk Scoring

Computes a normalized risk score (0–100) using trained ML model.

Higher scores indicate riskier driving patterns.

3. Dynamic Premium Calculation

Adjusts premiums proportionally to risk score.

Adds contextual multipliers for environmental conditions (e.g., weather, night driving).

Safe drivers earn small discounts and bonus reward points.

4. Dashboard

User-friendly Streamlit app.

Interactive sliders and visual feedback.

Displays real-time risk score, base premium, final premium, and behavior summary.

API Docs: http://127.0.0.1:8000/docs
Dashboard: http://localhost:8501

Future Enhancements

Real Telematics Integration: Connect actual GPS/accelerometer data from smartphones or OBD devices.

Database Integration: Persist user data and trip history using AWS DynamoDB or PostgreSQL.

Model Optimization: Explore XGBoost, LightGBM, and ensemble learning for risk prediction.

User Authentication: Enable login-based driver profiles and personalized dashboards.

Live Trip Analytics: Introduce visual maps and session-based driving feedback.

Scalability Enhancements: Containerize using Docker and deploy via AWS ECS or Kubernetes.

Conclusion

This project demonstrates a complete end-to-end implementation of an AI-powered insurance pricing engine, combining data simulation, machine learning, API development, and frontend visualization in a scalable, modular design.

It reflects the practical application of AI in insurance technology, aligning with modern InsurTech trends toward transparency, fairness, and personalization.

The system effectively integrates analytical modeling, software engineering, and product design — making it an ideal foundation for enterprise-scale telematics-based insurance solutions.



Github repo- https://github.com/vardhankaranam25/insurity.git


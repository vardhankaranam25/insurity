


source venv/bin/activate


echo "🚀 Starting FastAPI backend..."
nohup python -m uvicorn src.api.app:app --reload > backend.log 2>&1 &


sleep 3


echo "🎨 Launching Streamlit dashboard..."
streamlit run dashboard/streamlit_app.py

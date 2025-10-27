from fastapi import FastAPI
from pydantic import BaseModel
from src.pricing_engine import calculate_premium

app = FastAPI(
    title="Telematics Insurance API",
    description="API that calculates driver risk score and dynamic insurance premium",
    version="1.0"
)

# Request schema
class DriverData(BaseModel):
    avg_speed: float
    avg_acceleration: float
    brake_events: int
    distance_km: float
    night_drive: int


@app.get("/")
def home():
    return {"message": "Welcome to the Telematics Insurance API 🚗"}


@app.post("/calculate_premium")
def get_premium(data: DriverData):
    """
    Takes driver data and returns calculated premium and risk score.
    """
    result = calculate_premium(data.dict())
    return result

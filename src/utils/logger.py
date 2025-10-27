import sqlite3
from datetime import datetime
import os


os.makedirs("data/logs", exist_ok=True)

DB_PATH = "data/logs/logs.db"

def init_db():
    """Create the table if it doesn't exist"""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS premium_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT,
            avg_speed REAL,
            avg_acceleration REAL,
            brake_events INTEGER,
            distance_km REAL,
            night_drive INTEGER,
            risk_score REAL,
            final_premium REAL,
            note TEXT
        )
        """)
        conn.commit()

def log_premium(driver_data, risk_score, final_premium, note):
    """Insert a new log record"""
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""
        INSERT INTO premium_logs (
            timestamp, avg_speed, avg_acceleration, brake_events, distance_km,
            night_drive, risk_score, final_premium, note
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            driver_data["avg_speed"],
            driver_data["avg_acceleration"],
            driver_data["brake_events"],
            driver_data["distance_km"],
            driver_data["night_drive"],
            risk_score,
            final_premium,
            note
        ))
        conn.commit()

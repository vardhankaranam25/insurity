import sqlite3
import pandas as pd

DB_PATH = "data/logs/logs.db"

def get_all_logs():
    """Fetch all premium log records from SQLite DB"""
    try:
        conn = sqlite3.connect(DB_PATH)
        df = pd.read_sql_query("SELECT * FROM premium_logs ORDER BY id DESC", conn)
        conn.close()
        return df
    except Exception as e:
        print(f"⚠️ Failed to read logs: {e}")
        return pd.DataFrame()

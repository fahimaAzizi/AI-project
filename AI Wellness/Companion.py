from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List
import openai
import sqlite3
import os

# Initialize FastAPI app
app = FastAPI()

# Middleware for CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# OpenAI API Key (Secure this in production!)
openai.api_key = os.getenv("OPENAI_API_KEY")

# SQLite Database Setup
conn = sqlite3.connect("wellness.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS checkins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user TEXT,
        mood TEXT,
        sleep_hours REAL,
        hydration INT,
        activity TEXT,
        notes TEXT,
        timestamp TEXT
    )
''')
conn.commit()

# Pydantic Model for Check-In
timestamp_now = lambda: datetime.utcnow().isoformat()

class CheckIn(BaseModel):
    user: str
    mood: str
    sleep_hours: float
    hydration: int
    activity: str
    notes: Optional[str] = ""
    timestamp: Optional[str] = timestamp_now()

# Helper: GPT-4 Based Wellness Tip Generator
def generate_tip(mood, sleep_hours, hydration, activity):
    prompt = f"""
    User's mood: {mood}
    Sleep hours: {sleep_hours}
    Water intake (glasses): {hydration}
    Activity today: {activity}

    Based on the above, give a short motivational wellness tip. Avoid repeating the question. Keep it friendly and caring.
    """
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful health and wellness assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    return response["choices"][0]["message"]["content"]

# Endpoint: Daily Check-in
@app.post("/check_in/")
def check_in(data: CheckIn):
    # Save data to DB
    cursor.execute('''
        INSERT INTO checkins (user, mood, sleep_hours, hydration, activity, notes, timestamp)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (data.user, data.mood, data.sleep_hours, data.hydration, data.activity, data.notes, data.timestamp))
    conn.commit()

    # Generate AI tip
    ai_tip = generate_tip(data.mood, data.sleep_hours, data.hydration, data.activity)

    return JSONResponse({
        "message": "Check-in successful!",
        "ai_tip": ai_tip,
        "timestamp": data.timestamp
    })

# Endpoint: Get all check-ins for a user
@app.get("/check_ins/{user}")
def get_check_ins(user: str):
    cursor.execute("SELECT * FROM checkins WHERE user=? ORDER BY timestamp DESC", (user,))
    rows = cursor.fetchall()
    entries = [
        {
            "id": r[0], "user": r[1], "mood": r[2], "sleep_hours": r[3],
            "hydration": r[4], "activity": r[5], "notes": r[6], "timestamp": r[7]
        } for r in rows
    ]
    return {"check_ins": entries}

# Root
@app.get("/")
def root():
    return {"message": "Welcome to the AI Wellness Companion!"}

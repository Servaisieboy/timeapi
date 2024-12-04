
from flask import Flask, jsonify
from datetime import datetime
import pytz

app = Flask(__name__)

def get_current_time(city):
    timezones = {
        "New York": "America/New_York",
        "Porto": "Europe/Lisbon"
    }
    tz = pytz.timezone(timezones[city])
    city_time = datetime.now(tz).strftime("%H:%M")
    return city_time

@app.route("/api/time/newyork", methods=["GET"])
def time_new_york():
    time = get_current_time("New York")
    return jsonify({"time": time})

@app.route("/api/time/porto", methods=["GET"])
def time_porto():
    time = get_current_time("Porto")
    return jsonify({"time": time})

# Export the app as a callable for Vercel
app = app

from flask import Flask
from datetime import datetime
import pytz

app = Flask(__name__)

def get_current_time(city):
    """
    Haal de huidige tijd op voor een specifieke stad.
    """
    timezones = {
        "New York": "America/New_York",
        "Porto": "Europe/Lisbon"
    }
    tz = pytz.timezone(timezones[city])
    city_time = datetime.now(tz).strftime("%H:%M")
    return city_time

@app.route("/api/time/newyork", methods=["GET"])
def time_new_york():
    """
    API-endpoint om de tijd in New York te retourneren als platte tekst.
    """
    time = get_current_time("New York")
    return time, 200, {'Content-Type': 'text/plain'}

@app.route("/api/time/porto", methods=["GET"])
def time_porto():
    """
    API-endpoint om de tijd in Porto te retourneren als platte tekst.
    """
    time = get_current_time("Porto")
    return time, 200, {'Content-Type': 'text/plain'}

# Maak de app beschikbaar voor Vercel
app = app

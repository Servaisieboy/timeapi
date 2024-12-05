from flask import Flask, jsonify
from flask_cors import CORS
from datetime import datetime
import pytz
import requests

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def get_current_time(city):
    """Get the current time for the given city."""
    timezones = {
        "New York": "America/New_York",
        "Porto": "Europe/Lisbon"
    }
    tz = pytz.timezone(timezones[city])
    city_time = datetime.now(tz).strftime("%H:%M")
    return city_time

def get_temperature(city):
    """Get the current temperature for the given city."""
    # MetaWeather API uses location WOEIDs (Where On Earth IDs)
    city_mapping = {
        "New York": 2459115,
        "Porto": 2735943
    }
    try:
        woeid = city_mapping[city]
        url = f"https://www.metaweather.com/api/location/{woeid}/"
        response = requests.get(url)
        data = response.json()
        
        # Debugging: Log the response to see what is returned
        print(f"Response for {city}: {data}")
        
        if response.status_code == 200:
            # Get the temperature in Celsius from the first forecast
            return data["consolidated_weather"][0]["the_temp"]
        else:
            return None  # Return None if API request fails
    except Exception as e:
        print(f"Error fetching temperature for {city}: {e}")  # Log the error
        return None

@app.route("/api/time/newyork", methods=["GET"])
def time_new_york():
    """API endpoint to get the current time and temperature in New York."""
    time = get_current_time("New York")
    temperature = get_temperature("New York")
    return jsonify({
        "time": time, 
        "temperature": f"{round(temperature)}°C" if temperature else "Unavailable"
    })

@app.route("/api/time/porto", methods=["GET"])
def time_porto():
    """API endpoint to get the current time and temperature in Porto."""
    time = get_current_time("Porto")
    temperature = get_temperature("Porto")
    return jsonify({
        "time": time, 
        "temperature": f"{round(temperature)}°C" if temperature else "Unavailable"
    })

# Export the app as a callable for Vercel
app = app

import requests
import json
import os
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")  # your variable name in .env

# Set location (can be city name, zip, lat,long)
location = input("Enter city name: ") 

# Construct API URL
url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={location}&aqi=no"

try:
    response = requests.get(url)
    response.raise_for_status()  # Raise error for bad status

    # Parse JSON response
    weather_data = response.json()

    # Save to a local JSON file
    with open("weather_data.json", "w") as f:
        json.dump(weather_data, f, indent=4)

    print("✅ Weather data saved to weather_data.json")

except requests.exceptions.HTTPError as err:
    print("❌ HTTP error occurred:", err)
except Exception as e:
    print("❌ Other error occurred:", e)
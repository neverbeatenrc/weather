from flask import Flask, request, jsonify, render_template
import requests
import json
import os
from dotenv import load_dotenv
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend JS to access this API

load_dotenv()
API_KEY = os.getenv("API_KEY")

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/weather", methods=["POST"])
def get_weather():
    data = request.get_json()
    city = data.get("city")

    url = f"https://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"

    try:
        response = requests.get(url)
        response.raise_for_status()
        weather_data = response.json()

        with open("weather_data.json", "w") as f:
            json.dump(weather_data, f, indent=4)

        return jsonify({"status": "success", "data": weather_data})

    except requests.exceptions.HTTPError as err:
        return jsonify({"status": "error", "message": str(err)})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

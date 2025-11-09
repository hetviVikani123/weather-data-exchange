from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# --- Environment Variables ---
BASEX_REST_URL = os.getenv("BASEX_REST_URL", "http://admin:admin@localhost:8984")
BASEX_DB = os.getenv("BASEX_DB", "weatherDB")
CITY_NAME = os.getenv("CITY_NAME", "CityA")


# --- Route: Upload XML weather data ---
@app.route('/upload', methods=['POST'])
def upload_data():
    city = request.args.get('city', CITY_NAME)
    xml_data = request.data

    if not xml_data:
        return jsonify({"error": "No XML data received"}), 400

    # Upload XML to BaseX database
    response = requests.post(f"{BASEX_REST_URL}/rest/{BASEX_DB}", data=xml_data)

    if response.status_code in [200, 201]:
        return jsonify({"message": f"Data uploaded successfully for {city}"}), 201
    else:
        return jsonify({"error": "Failed to upload data"}), response.status_code


# --- Route: Fetch all city weather data ---
@app.route('/weather', methods=['GET'])
def get_weather():
    response = requests.get(f"{BASEX_REST_URL}/rest/{BASEX_DB}")

    if response.status_code == 200:
        return response.text, 200, {'Content-Type': 'application/xml'}
    else:
        return jsonify({"error": "Failed to fetch data"}), response.status_code


# --- Route: Health check ---
@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": f"{CITY_NAME} Weather Service is running!"})


if __name__ == '__main__':
    app.run(debug=True, port=5001)

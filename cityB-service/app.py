import os
from flask import Flask, request, Response
import xml.etree.ElementTree as ET
import datetime

app = Flask(__name__)

CITY_NAME = "CityB"
PORT = 5001

def generate_weather_xml(city, temp, hum, wind, cond):
    report = ET.Element("weatherReport")
    ET.SubElement(report, "city").text = city
    ET.SubElement(report, "date").text = datetime.date.today().isoformat()
    ET.SubElement(report, "temperature", unit="C").text = str(temp)
    ET.SubElement(report, "humidity", unit="%").text = str(hum)
    ET.SubElement(report, "windSpeed", unit="km/h").text = str(wind)
    ET.SubElement(report, "condition").text = cond
    return ET.tostring(report, encoding="utf-8")

@app.route("/")
def home():
    return {"message": f"{CITY_NAME} Weather Service is running!"}

@app.route("/publish", methods=["GET"])
def publish_weather():
    xml_data = generate_weather_xml(CITY_NAME, 19.2, 72, 9, "Cloudy")
    return Response(xml_data, mimetype="application/xml")

@app.route("/upload", methods=["POST"])
def upload_weather():
    xml_data = request.data.decode("utf-8")
    city = request.args.get("city", CITY_NAME)
    filename = f"received_from_{city}.xml"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(xml_data)
    return {"message": f"Data uploaded successfully for {city}"}, 200

if __name__ == "__main__":
    app.run(port=PORT)

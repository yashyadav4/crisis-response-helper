from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import requests
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)
CORS(app)

def get_nearby_places(lat, lon):
    try:
        query_url = f"https://nominatim.openstreetmap.org/reverse?format=json&lat={lat}&lon={lon}&zoom=18&addressdetails=1"
        response = requests.get(query_url, headers={"User-Agent": "CrisisHelper"})
        data = response.json()
        display = []
        if 'address' in data:
            if 'hospital' in data['address']:
                display.append("Hospital: " + data['address']['hospital'])
            if 'police' in data['address']:
                display.append("Police: " + data['address']['police'])
        return display
    except Exception:
        return []

@app.route("/crisis", methods=["POST"])
def handle_crisis():
    data = request.get_json()
    crisis_type = data.get("type", "emergency")
    lat = data.get("lat")
    lon = data.get("lon")

    prompt = f"You are a survival expert. A person is in a {crisis_type}. Give them calm, step-by-step survival instructions."

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a calm, helpful survival expert."},
                {"role": "user", "content": prompt}
            ]
        )
        reply = response['choices'][0]['message']['content']
        places = get_nearby_places(lat, lon)
        return jsonify({"response": reply, "places": places})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

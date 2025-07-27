import json
from flask import Flask, request
import requests

app = Flask(__name__)

SUPABASE_URL = "https://qyoyhnssaxoategnybwo.supabase.co/rest/v1/sensor_readings"
SUPABASE_KEY = "sb_publishable_U7X9IXqIIyEa19ZPrQ_9Fg_wydXLrt-"

@app.route("/", methods=["POST"])
def proxy():
    data = request.get_json()
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }
    response = requests.post(SUPABASE_URL, json=data, headers=headers)
    return {"status": response.status_code, "supabase_response": response.text}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)



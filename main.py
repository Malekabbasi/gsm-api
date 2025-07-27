from flask import Flask, request, jsonify
import requests
import os

app = Flask(__name__)

# 🔐 Supabase credentials
SUPABASE_URL = "https://qyoyhnssaxoategnybwo.supabase.co"
SUPABASE_TABLE = "sensor_readings"
SUPABASE_KEY = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InF5b3lobnNzYXhvYXRlZ255YndvIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTI1MDIxMTQsImV4cCI6MjA2ODA3ODExNH0.bWn3ODbnK3F2prisQlTX4HE9kmDmC0kLHZS-qHSNGxY"
SUPABASE_ENDPOINT = f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}"

@app.route("/", methods=["GET"])
def home():
    return "✅ Flask API with Supabase Ready", 200

@app.route("/api", methods=["POST"])
def receive_data():
    try:
        data = request.json
        print("📥 Données reçues:", data)

        # ➤ Send data to Supabase
        headers = {
            "Content-Type": "application/json",
            "apikey": SUPABASE_KEY.split(" ", 1)[1],  # remove 'Bearer '
            "Authorization": SUPABASE_KEY
        }

        response = requests.post(SUPABASE_ENDPOINT, json=data, headers=headers)
        print("📡 Supabase response:", response.status_code, response.text)

        if response.status_code in [200, 201]:
            return jsonify({"status": "success", "message": "Data sent to Supabase"}), 200
        else:
            return jsonify({"status": "error", "supabase_response": response.text}), 500

    except Exception as e:
        print("❌ Erreur:", e)
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
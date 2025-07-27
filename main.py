from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

SUPABASE_URL = "https://qyoyhnssaxoategnybwo.supabase.co"
SUPABASE_TABLE = "sensor_readings"
SUPABASE_API_KEY = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."  # 🔐 حط المفتاح كامل

@app.route("/", methods=["GET"])
def home():
    return "✅ Replit Flask API Ready", 200

@app.route("/api", methods=["POST"])
def receive_data():
    try:
        data = request.json
        print("📥 Données reçues:", data)

        # ➤ إرسال إلى Supabase
        headers = {
            "apikey": SUPABASE_API_KEY,
            "Authorization": SUPABASE_API_KEY,
            "Content-Type": "application/json"
        }

        supabase_response = requests.post(
            f"{SUPABASE_URL}/rest/v1/{SUPABASE_TABLE}",
            headers=headers,
            json=data
        )

        print("📤 Supabase response:", supabase_response.status_code, supabase_response.text)

        if supabase_response.status_code in [200, 201]:
            return jsonify({"status": "success"}), 200
        else:
            return jsonify({"status": "supabase_error", "details": supabase_response.text}), 500

    except Exception as e:
        print("❌ Erreur:", e)
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "✅ Replit Flask API Ready", 200

@app.route("/api", methods=["POST"])
def receive_data():
    try:
        data = request.json
        print("📥 Données reçues:", data)
        return jsonify({"status": "success"}), 200
    except Exception as e:
        print("❌ Erreur:", e)
        return jsonify({"status": "error", "message": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)

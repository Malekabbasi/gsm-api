from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["POST"])
def receive_data():
    try:
        data = request.get_json()
        print("✅ Données reçues :", data)

        # Traitement ou enregistrement optionnel
        return jsonify({"status": "success", "message": "Données reçues"}), 200
    except Exception as e:
        print("❌ Erreur :", e)
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route("/", methods=["GET"])
def home():
    return "API GSM de réception prête", 200

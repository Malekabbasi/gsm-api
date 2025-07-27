from flask import Flask, request
import requests

app = Flask(__name__)

# ✅ Paramètres Supabase
SUPABASE_URL = "https://qyoyhnssaxoategnybwo.supabase.co/rest/v1/sensor_readings"
SUPABASE_KEY = "sb_publishable_U7X9IXqIIyEa19ZPrQ_9Fg_wydXLrt-"

# ✅ Point d'entrée principal
@app.route("/api", methods=["POST"])
def proxy_api():
    data = request.get_json()
    
    # ✅ Entêtes pour Supabase
    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json"
    }

    # ✅ Requête POST vers Supabase
    response = requests.post(SUPABASE_URL, json=data, headers=headers)
    
    return response.text, response.status_code


# ✅ Pour Render (nécessaire pour lancer le serveur)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)

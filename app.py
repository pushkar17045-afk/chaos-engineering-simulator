from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/request")
def handle_request():
    try:
        r = requests.get("http://service_b:5001/process", timeout=2)
        return jsonify({"status": "ok", "data": r.json()})
    except Exception as e:
        return jsonify({"status": "degraded", "error": str(e)}), 503

app.run(host="0.0.0.0", port=5000)

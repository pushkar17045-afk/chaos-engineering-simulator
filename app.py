import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "running",
        "project": "Chaos Engineering Simulator",
        "services": ["service_a", "service_b", "service_c"]
    })

@app.route("/docs")
def docs():
    return {
        "endpoints": [
            "GET /",
            "GET /docs",
            "GET /health",
            "POST /inject/latency",
            "POST /inject/crash"
        ]
    }

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)

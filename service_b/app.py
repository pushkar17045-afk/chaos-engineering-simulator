from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

@app.route("/process")
def process():
    time.sleep(random.uniform(0.1, 0.3))
    return jsonify({"result": "processed"})

app.run(host="0.0.0.0", port=5001)

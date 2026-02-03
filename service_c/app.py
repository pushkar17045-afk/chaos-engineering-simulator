from flask import Flask, request

app = Flask(__name__)

@app.route("/log", methods=["POST"])
def log():
    print(request.json)
    return {"status": "logged"}

app.run(host="0.0.0.0", port=5002)

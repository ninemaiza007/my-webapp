from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "Server Running"

@app.route("/api")
def api():
    return jsonify({"message": "Hello from Python on Render!"})

if __name__ == "__main__":
    app.run()

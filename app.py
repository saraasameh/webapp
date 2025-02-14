from flask import Flask, request, jsonify, render_template
import json
import os

app = Flask(__name__)

# Load user data from JSON
def load_data():
    with open("data.json", "r") as file:
        return json.load(file)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user_id = request.form.get("user_id")
        data = load_data()
        if user_id in data:
            return jsonify(data[user_id])  # Return username and password
        else:
            return jsonify({"error": "User ID not found"})
    return render_template("index.html")

if __name__ == "__main__":
    from waitress import serve
    port = int(os.environ.get("PORT", 8080))
    serve(app, host="0.0.0.0", port=port)
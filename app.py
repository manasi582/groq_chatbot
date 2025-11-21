# app.py
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
from chatbot import chatbot  # import your function

# ensure .env is loaded for Flask as well (optional, already loaded in chatbot.py)
load_dotenv(dotenv_path="/Users/manasiashokpatil/Desktop/projects/chatbot_project/.env")

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json(force=True)
    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "empty message"}), 400

    try:
        reply = chatbot(message)
        return jsonify({"reply": reply})
    except Exception as e:
        # Return server error details in JSON for easier debugging
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    # change host= to 0.0.0.0 only when you want external access
    app.run(debug=True, port=5000)

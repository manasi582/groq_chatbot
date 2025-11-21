# app.py

from flask import Flask, render_template, request, jsonify, Response
from dotenv import load_dotenv
import os

# Load .env normally
load_dotenv()

from chatbot import chatbot, chatbot_stream

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/ask", methods=["POST"])
def ask():
    """
    Non-streaming response for fallback
    """
    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    message = data.get("message", "").strip()
    if not message:
        return jsonify({"error": "empty message"}), 400

    reply = chatbot(message)
    return jsonify({"reply": reply})


@app.route("/ask_stream", methods=["POST"])
def ask_stream():
    """
    Streaming endpoint — sends chunks as they arrive.
    """

    try:
        data = request.get_json(force=True)
    except Exception:
        return jsonify({"error": "Invalid JSON"}), 400

    message = data.get("message", "").strip()
    if not message:
        return Response("empty message", status=400)

    def generate():
        for token in chatbot_stream(message):
            yield token

    return Response(generate(), mimetype="text/plain")


if __name__ == "__main__":
    app.run(debug=True, port=5000)

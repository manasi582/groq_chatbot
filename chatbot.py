# chatbot.py

import os
from dotenv import load_dotenv
from groq import Groq

# Load .env securely
load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chatbot(message):
    """Send a message to Groq LLM and return the reply as text."""
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content

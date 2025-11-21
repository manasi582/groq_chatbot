

import os
from dotenv import load_dotenv

# Load .env using absolute path (same method that worked in your test)
load_dotenv(dotenv_path="/Users/manasiashokpatil/Desktop/projects/chatbot_project/.env")

from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chatbot(message):
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content

# Chat loop
while True:
    msg = input("You: ")
    if msg.lower() in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye!")
        break

    reply = chatbot(msg)
    print("Chatbot:", reply)




""" 

# chatbot.py
import os
from dotenv import load_dotenv

# Load .env using absolute path (same method that worked for you)
load_dotenv(dotenv_path="/Users/manasiashokpatil/Desktop/projects/chatbot_project/.env")

from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def chatbot(message):
    """
"""Send `message` to Groq and return the assistant reply as text.
   
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": message}]
    )
    return response.choices[0].message.content 
"""
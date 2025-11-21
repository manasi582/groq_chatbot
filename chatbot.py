# chatbot.py

import os
from dotenv import load_dotenv
from groq import Groq, GroqError

# Load .env from current directory
load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
if not API_KEY:
    raise ValueError("GROQ_API_KEY is missing. Add it to your .env file.")

client = Groq(api_key=API_KEY)

# Global conversation memory
conversation_history = [
    {"role": "system", "content": "You are a helpful AI assistant."}
]

def chatbot(message):
    """
    Handle multi-turn conversation.
    Append user message to history, send to Groq LLM, append reply, return text.
    """

    # Add user message to conversation
    conversation_history.append({"role": "user", "content": message})

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=conversation_history,
            temperature=0.8,
            max_tokens=300
        )
    except GroqError as e:
        return f"[Groq API Error] {str(e)}"
    except Exception as e:
        return f"[Unexpected Error] {str(e)}"

    reply = response.choices[0].message.content

    # Save reply to memory
    conversation_history.append({"role": "assistant", "content": reply})

    return reply


def chatbot_stream(message):
    """
    Stream responses token-by-token.
    """

    # Add user message
    conversation_history.append({"role": "user", "content": message})

    try:
        stream = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=conversation_history,
            temperature=0.8,
            max_tokens=300,
            stream=True,
        )

        full_reply = ""

        for chunk in stream:
            if chunk.choices:
                delta = chunk.choices[0].delta
                if hasattr(delta, "content") and delta.content:
                    token = delta.content
                    full_reply += token
                    yield token   # STREAM token to Flask route

        # Save final reply to memory
        conversation_history.append({"role": "assistant", "content": full_reply})

    except GroqError as e:
        yield f"[Groq API Error] {str(e)}"
    except Exception as e:
        yield f"[Unexpected Error] {str(e)}"

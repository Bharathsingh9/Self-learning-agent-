import json
import re
from groq import Groq
import sys
import os

# Add parent dir to path to import config
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from config import Config

# Initialize Groq client
client = Groq(api_key=Config.GROQ_API_KEY)

def generate_response(prompt: str, retries: int = Config.MAX_RETRIES) -> str:
    """
    Globally reusable wrapper for Groq LLM generation.
    Handles basic retries and missing outputs using the Groq SDK.
    """
    for attempt in range(retries):
        try:
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": prompt,
                    }
                ],
                model=Config.MODEL_NAME,
            )

            if chat_completion and chat_completion.choices:
                return chat_completion.choices[0].message.content.strip()

        except Exception as e:
            print(f"LLM error on attempt {attempt+1}: {e}")

    return "ERROR: Failed to generate response"

def extract_json(text: str):
    """
    Robustly extract and parse JSON from string.
    Useful when LLMs return JSON fenced in markdown blocks.
    """
    try:
        return json.loads(text)
    except Exception:
        # Clean markdown wrappers first
        cleaned = re.sub(r"```json|```", "", text).strip()
        # Match JSON like {...} or [...] across lines
        match = re.search(r"\{[\s\S]*\}|\[[\s\S]*\]", cleaned)
        if match:
            return json.loads(match.group())
        raise ValueError("Invalid JSON output")

from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

api_key = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL")

if not api_key:
    raise ValueError("OPENROUTER_API_KEY not found.")

if not MODEL:
    raise ValueError("MODEL not found.")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

print("=" * 50)
print("OpenRouter CLI Chatbot")
print("Type 'exit' to quit")
print("=" * 50)

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        reply = response.choices[0].message.content

        print("\nAssistant:", reply)

    except Exception as e:
        print("\nError:", e)
from config import client, MODEL
from prompts import SYSTEM_PROMPT

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
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
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
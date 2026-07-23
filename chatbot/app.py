from config import client, MODEL
from prompts import SYSTEM_PROMPT

print("=" * 50)
print("OpenRouter CLI Chatbot")
print("Type 'exit' to quit")
print("=" * 50)

# Initialize conversation history
messages = [
    {
        "role": "system",
        "content": SYSTEM_PROMPT
    }
]

while True:

    user_input = input("\nYou: ")

    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    # Add user's message
    messages.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=messages
        )

        reply = response.choices[0].message.content

        print("\nAssistant:", reply)

        # Save assistant's reply
        messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

    except Exception as e:
        print("\nError:", e)
from config import client, MODEL
from prompts import SYSTEM_PROMPT
from commands import (
    is_command,
    handle_help,
    build_summary_prompt,
)

print("=" * 50)
print("OpenRouter CLI Chatbot")
print("Type 'exit' to quit")
print("=" * 50)

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

    # Command Handling
    if is_command(user_input):

        if user_input == "/help":

            print(handle_help())
            continue

        elif user_input.startswith("/summarize"):

            topic = user_input.replace("/summarize", "", 1).strip()

            if not topic:
                print("Please provide a topic.")
                continue

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
                            "content": build_summary_prompt(topic)
                        }
                    ]
                )

                print("\nAssistant:")
                print(response.choices[0].message.content)

            except Exception as e:
                print("\nError:", e)

            continue

        else:

            print("Unknown command. Type /help")
            continue

    # Normal Conversation
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

        messages.append(
            {
                "role": "assistant",
                "content": reply
            }
        )

    except Exception as e:
        print("\nError:", e)
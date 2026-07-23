import json


def is_command(user_input):
    """
    Check whether the user entered a command.
    """
    return user_input.startswith("/")


def handle_help():
    """
    Display available chatbot commands.
    """
    return """
Available Commands

/help
    Display available commands.

/summarize <topic>
    Generate a short summary in JSON format.

exit
    Close the chatbot.
"""


def build_summary_prompt(topic):
    """
    Create the prompt for the summarization command.
    """
    return f"""
Summarize the following topic.

Topic:
{topic}

Return ONLY valid JSON in this format:

{{
    "command": "summarize",
    "topic": "{topic}",
    "summary": "<summary>"
}}

Do not include markdown.
Do not include explanations.
Return JSON only.
"""
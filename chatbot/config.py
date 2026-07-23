import os
from pathlib import Path

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv(dotenv_path=Path(__file__).parent / ".env")

API_KEY = os.getenv("OPENROUTER_API_KEY")
MODEL = os.getenv("MODEL")

if not API_KEY:
    raise ValueError("OPENROUTER_API_KEY not found.")

if not MODEL:
    raise ValueError("MODEL not found.")

client = OpenAI(
    api_key=API_KEY,
    base_url="https://openrouter.ai/api/v1"
)
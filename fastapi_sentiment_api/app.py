from fastapi import FastAPI
from transformers import pipeline

# Create the FastAPI application
app = FastAPI()

# Load the pretrained sentiment analysis model
classifier = pipeline(
    task="sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

# Root endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to the Sentiment Analysis API!"
    }
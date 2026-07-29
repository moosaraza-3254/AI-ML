from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

# Create the FastAPI application
app = FastAPI()

# Load the pretrained sentiment analysis model
classifier = pipeline(
    task="sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

# Request model
class SentimentRequest(BaseModel):
    text: str

# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to the Sentiment Analysis API!"
    }

# Prediction endpoint
@app.post("/predict")
def predict(request: SentimentRequest):
    result = classifier(request.text)

    return {
        "label": result[0]["label"],
        "score": result[0]["score"]
    }
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI(
    title="Sentiment Analysis API",
    description="A REST API for sentiment analysis using Hugging Face Transformers.",
    version="1.0.0"
)

classifier = pipeline(
    task="sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)


class SentimentRequest(BaseModel):
    text: str


class SentimentResponse(BaseModel):
    input_text: str
    sentiment: str
    confidence: float


@app.get("/")
def home():
    return {
        "message": "Welcome to the Sentiment Analysis API!"
    }


@app.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest):
    result = classifier(request.text)

    return SentimentResponse(
        input_text=request.text,
        sentiment=result[0]["label"],
        confidence=result[0]["score"]
    )
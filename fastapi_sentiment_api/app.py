from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

# Create the FastAPI application
app = FastAPI(
    title="Sentiment Analysis API",
    description="A REST API for sentiment analysis using Hugging Face Transformers.",
    version="1.0.0"
)

# Load the pretrained sentiment analysis model
classifier = pipeline(
    task="sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

# Request model
class SentimentRequest(BaseModel):
    text: str


# Response model
class SentimentResponse(BaseModel):
    input_text: str
    sentiment: str
    confidence: float


# Home endpoint
@app.get("/")
def home():
    return {
        "message": "Welcome to the Sentiment Analysis API!"
    }


# Prediction endpoint
@app.post("/predict", response_model=SentimentResponse)
def predict(request: SentimentRequest):
    # Validate input
    if not request.text.strip():
        raise HTTPException(
            status_code=400,
            detail="Input text cannot be empty."
        )

    # Generate prediction
    result = classifier(request.text)

    # Return structured response
    return SentimentResponse(
        input_text=request.text,
        sentiment=result[0]["label"],
        confidence=result[0]["score"]
    )
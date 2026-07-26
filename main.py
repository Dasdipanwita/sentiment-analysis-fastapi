from fastapi import FastAPI, HTTPException

from schemas import Review
from model import analyze_sentiment


app = FastAPI(
    title="Sentiment Analysis API",
    description="Sentiment classification using DistilBERT and FastAPI",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "message": "Sentiment Analysis API is running"
    }


@app.post("/predict")
def predict_sentiment(review: Review):

    text = review.text.strip()

    if not text:
        raise HTTPException(
            status_code=400,
            detail="Text cannot be empty"
        )

    result = analyze_sentiment(text)

    return {
        "text": text,
        "sentiment": result["sentiment"],
        "confidence": result["confidence"]
    }
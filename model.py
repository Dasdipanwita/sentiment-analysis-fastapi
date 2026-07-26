from transformers import pipeline

sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)


def analyze_sentiment(text):
    result = sentiment_model(text)[0]

    return {
        "sentiment": result["label"],
        "confidence": round(result["score"], 4)
    }
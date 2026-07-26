from transformers import pipeline

sentiment_model = pipeline(
    "sentiment-analysis",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)

text = input("Enter your review: ")

result = sentiment_model(text)

print(result)
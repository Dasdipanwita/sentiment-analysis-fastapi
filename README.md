# Sentiment Analysis API

A simple NLP-based Sentiment Analysis REST API built with FastAPI and a pretrained DistilBERT model from Hugging Face.

The API accepts user text and predicts whether the sentiment is POSITIVE or NEGATIVE along with a confidence score.

## Features

- Sentiment classification
- POSITIVE and NEGATIVE predictions
- Confidence score
- REST API using FastAPI
- Request validation using Pydantic
- Empty/whitespace input handling
- Swagger UI for API testing

## Tech Stack

- Python
- FastAPI
- Hugging Face Transformers
- DistilBERT
- PyTorch
- Pydantic
- Uvicorn

## Model

This project uses the pretrained sentiment classification model:

`distilbert-base-uncased-finetuned-sst-2-english`

The model is already fine-tuned for binary sentiment classification. This project focuses on model integration and serving the model through a REST API.

## Project Structure

    Sentiment Analysis/
    ├── main.py
    ├── model.py
    ├── schemas.py
    ├── requirements.txt
    ├── README.md
    └── .gitignore

## Installation

Clone the repository and install the dependencies:

    pip install -r requirements.txt

## Run the API

Start the FastAPI server:

    python -m uvicorn main:app --reload

Then open the Swagger UI at:

    http://127.0.0.1:8000/docs

## API Endpoint

### POST /predict

Example request:

    {
      "text": "I really love this product"
    }

Example response:

    {
      "text": "I really love this product",
      "sentiment": "POSITIVE",
      "confidence": 0.9999
    }

## Input Validation

Empty or whitespace-only text is rejected with HTTP status code 400.

Example:

    {
      "text": "   "
    }

Response:

    {
      "detail": "Text cannot be empty"
    }
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Load a tiny, pre-trained NLP model for sentiment analysis
evaluator = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

class TextInput(BaseModel):
    text: str

@app.post("/evaluate")
def evaluate_text(input_data: TextInput):
    # This simulates evaluating a Generative AI's response
    result = evaluator(input_data.text)[0]
    return {"input": input_data.text, "score": result['score'], "label": result['label']}

@app.get("/")
def health_check():
    return {"status": "Container is running!"}
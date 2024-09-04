from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import AutoModelForSequenceClassification, AutoTokenizer
from loguru import logger
import torch
import re


# Init FastAPI
app = FastAPI()

# define input class
class Essay(BaseModel):
    text: str

model_path = "./models/model_weighted_training"

# Load model
model = AutoModelForSequenceClassification.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

def escape_quotes(text: str) -> str:
    return re.sub(r'(")', r'\"', text)

@app.post("/predict")
def predict(essay: Essay):
    try:
        logger.info("Received prediction request.")
        inputs = tokenizer(escape_quotes(essay.text), return_tensors="pt")
        with torch.no_grad():  
            outputs = model(**inputs)
            predictions = outputs.logits.argmax(dim=-1) + 1  # Add 1 because class is [0->5] while score is [1->6]

        score = predictions.item()
        
        logger.info(f"Prediction result: {score}")
        
        return {"score": score}
    except Exception as e:
        logger.error(f"Error during prediction: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

from pathlib import Path

import joblib
from fastapi import FastAPI
from pydantic import BaseModel, Field

PROJECT_ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_ROOT / "models" / "ticket_classifier.joblib"

model = joblib.load(MODEL_PATH)

app = FastAPI(
    title="AI Support Intelligence API",
    description="Predicts customer support ticket categories.",
    version="0.1.0",
)


class TicketRequest(BaseModel):
    subject: str = Field(min_length=1, max_length=300)
    description: str = Field(min_length=1, max_length=10000)


@app.get("/health")
def health_check():
    return {"status": "healthy", "model_loaded": True}


@app.post("/predict")
def predict_ticket(ticket: TicketRequest):
    text = f"{ticket.subject} {ticket.description}"
    prediction = model.predict([text])[0]

    return {
        "predicted_ticket_type": str(prediction)
    }


from fastapi.testclient import TestClient

from src.app import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {
        "status": "healthy",
        "model_loaded": True,
    }


def test_predict_endpoint():
    response = client.post(
        "/predict",
        json={
            "subject": "Payment issue",
            "description": (
                "I was charged twice for my subscription "
                "and need help getting a refund."
            ),
        },
    )

    assert response.status_code == 200
    assert "predicted_ticket_type" in response.json()


def test_predict_rejects_empty_subject():
    response = client.post(
        "/predict",
        json={
            "subject": "",
            "description": "I need help with my account.",
        },
    )

    assert response.status_code == 422

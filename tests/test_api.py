
from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json()["message"] == (
        "Kidney Disease ML API is running"
    )


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert response.json()["model_loaded"] is True


def test_invalid_prediction_input():
    response = client.post(
        "/predict",
        json={"age": "hello"}
    )
    assert response.status_code == 422

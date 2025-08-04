# test_main.py
import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_fibonacci_get():
    response = client.get("/fibonacci/10")
    assert response.status_code == 200
    assert response.json() == {"n": 10, "fibonacci": 55}

def test_fibonacci_post():
    response = client.post("/fibonacci", json={"n": 10})
    assert response.status_code == 200
    assert response.json() == {"n": 10, "fibonacci": 55}

def test_fibonacci_negative():
    response = client.get("/fibonacci/-1")
    assert response.status_code == 400

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

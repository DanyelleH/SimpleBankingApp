import pytest
from fastapi.testclient import TestClient
from app.main import app
from backend.app.models.user_model import create_user
from models.account import create_account

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


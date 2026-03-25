import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.schemas.user_schema import UserCreate
from app.controllers.account_controller import create_user_account


client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

# Test user creation, along with account creation
# def test_create_user_account(user_collection, account_collection):
#     #creating test user
#     user_data = UserCreate(name="John Doe", email="john@email.com")

#     result = create_user_account(user_collection, account_collection, user_data)

#     user_id = result["user"]["id"]
#     account_id = result["account"]["id"]

#     user = user_collection.find_one({"_id": ObjectId(user_id)})
#     account = account_collection.find_one({"_id": ObjectId(account_id)})

#     assert user is not None
#     assert account is not None
#     assert account["user_id"] == user_id
def test_create_user():
    user_data_payload = {
        "name": "John Doe",
        "email": "John.Doe@email.com"
    }
    response = client.post("/users", json=user_data_payload)
    assert response.status_code == 200
    response_data = response.json()

    # ensure the account [user_id] matches the user [_id]
    assert response_data["account"]["user_id"] == response_data["user"]["user_id"]
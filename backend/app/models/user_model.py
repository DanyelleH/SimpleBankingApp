# models/user.py
from app.config.database import db
from datetime import datetime

def create_user(username, password):
    user = {
        "username": username,
        "password": password,
    }
    result = db.users.insert_one(user)
    user["_id"] = result.inserted_id
    return user
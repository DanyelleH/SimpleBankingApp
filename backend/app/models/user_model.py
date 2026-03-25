from app.config.database import db
from datetime import datetime

def create_user(name, email):
    user = {
        "name": name,
        "email": email,
        "created_at": datetime.now().isoformat()
    }
    result = db.users.insert_one(user)
    return {
        "user_id": str(result.inserted_id),
        "name": user["name"],
        "email": user["email"],
        "created_at": user["created_at"]
    }   
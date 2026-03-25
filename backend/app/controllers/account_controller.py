from datetime import datetime
from app.config.database import db

def create_user_account(user_id):
    account = {
        "user_id": user_id,
        "balance": 0.0,
        "account_type": "CHECKING",
        "created_at": datetime.now().isoformat()
    }
    result = db.accounts.insert_one(account)
    return {
        "account_id": str(result.inserted_id),
        "user_id": str(user_id),
        "balance": account["balance"],
        "account_type": account["account_type"],
        "created_at": account["created_at"]
    }
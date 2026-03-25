from app.models.user_model import create_user
from app.controllers.account_controller import create_user_account

def create_user_and_account(name, email):
    user = create_user(name, email)
    account = create_user_account(user["user_id"])
    return {"user": user, "account": account}
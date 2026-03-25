from fastapi import FastAPI
from datetime import datetime
from app.config.database import user_collection, account_collection, transaction_collection
from app.routes.user_routes import router as user_router
app=FastAPI(title="Simple Banking Application", version="1.0.0")


# user = {
#     "name": "johndoe",
#     "email": "john.doe@email.com",
#     "created_at": datetime.now()
# }
# # insert a user -> this will generate a user_id in the database
# user_result = user_collection.insert_one(user)
# # create an account for the user -> this will generate an account_id in the database
# account = {
#     "user_id": str(user_result.inserted_id),
#     "balance": 0,
#     "account_type": "CHECKING",
#     "created_at": datetime.now()
# }
# # create account and tie it to the user
# account_result = account_collection.insert_one(account)
# # create a transaction for the account -> this will generate a transaction_id in the database
# transaction = {
#     "account_id": str(account_result.inserted_id),
#     "txn_type": "DEPOSIT",
#     "amount": 100,
#     "created_at": datetime.now()
# }
# transaction_collection.insert_one(transaction)
app.include_router(user_router, prefix="/users", tags=["users"])
@app.get("/health")
async def health_check():
    return {"status": "healthy"}
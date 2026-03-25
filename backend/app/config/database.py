# database.py
import os
from pymongo import MongoClient
from dotenv import load_dotenv
load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("MONGO_DB_NAME")]

#each model will have its own collection
user_collection = db["users"]
account_collection = db["accounts"]
transaction_collection = db["transactions"]
from fastapi import APIRouter, HTTPException
from app.schemas.user_schema import UserOut, UserCreate
from app.schemas.account_schema import AccountOut
from app.controllers.user_controller import create_user_and_account
from app.schemas.common_schema import UserAndAccountOut
from pydantic import BaseModel
from typing import Dict

router=APIRouter()

@router.post("/", response_model=UserAndAccountOut)
def create_user(user: UserCreate):
    result = create_user_and_account(user.name, user.email)
    return result
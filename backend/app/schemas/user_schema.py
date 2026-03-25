from pydantic import BaseModel

# on creation, we only need the name and email
class UserCreate(BaseModel):
    name: str
    email: str

# on output, we want to include the user_id and created_at timestamp
class UserOut(BaseModel):
    user_id: str
    name: str
    email: str
    created_at: str
from pydantic import BaseModel
from .user_schema import UserOut
from .account_schema import AccountOut
class UserAndAccountOut(BaseModel):
    user: UserOut
    account: AccountOut
python
from pydantic import BaseModel
from typing import Optional
from password_context import hasura_jwt_payload_validator
import datetime

class UserBase(BaseModel):
    email: str
    username: str
    password: str
    is_admin: bool = False

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    email: Optional[str] = None
    is_admin: Optional[bool] = None

class PasswordField(str):
    def __get__(self, instance, owner):
        if instance.current_password_hash:
            return hasura_jwt_payload_validator.verify_password(instance.current_password_hash, self)
        else:
            raise ValueError('Current password hash must be set')

class UserUpdate(UserBase):
    password: Optional[PasswordField]
    current_password_hash: Optional[str]

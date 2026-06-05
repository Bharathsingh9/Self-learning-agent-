python
# src/services/user.py
from typing import Dict, Optional
from pydantic import BaseModel
from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer
from jose import jwt
from datetime import datetime, timedelta
from src.core.config import settings
from src.database.database import SessionLocal, engine, DB session
from src.schemas.token import Token, TokenData
from src.crud.crud_user import crud_user
from src.models.user import User

# Define a Pydantic model for the User data
class UserBase(BaseModel):
    username: str
    email: Optional[str]
    password: Optional[str]

# Define a Pydantic model for the User data (with hashed password)
class UserCreate(BaseModel):
    username: str
    email: str
    password: str

# Define a Pydantic model for the User data (with hashed password)
class UserUpdate(BaseModel):
    username: Optional[str]
    email: Optional[str]
    password: Optional[str]

# Define a Pydantic model for the User data
class UserLogin(BaseModel):
    username: str
    password: str

# Define the OAuth2 scheme for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

# Define a function to authenticate the user
def authenticate_user(fake_db, username: str, password: str):
    user = crud_user.get_userByUsername(fake_db, username)
    if user and verify_password(password, user.password):
        return user
    return None

# Define a function to verify the password
def verify_password(plain_password, hashed_password):
    return plain_password == hashed_password

# Define a function to get the current user
def get_current_user(db: SessionLocal = Depends(session), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        token_data = TokenData(username=payload.get("sub"))
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Login expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")
    user = crud_user.get_userByUsername(db, token_data.username)
    if user:
        return user
    raise HTTPException(status_code=401, detail="User not found")

# Define a function to get the superuser
def get_super_user(db: SessionLocal = Depends(session), token: str = Depends(oauth2_scheme)):
    user = get_current_user(db, token)
    if user.is_superuser:
        return user
    raise HTTPException(status_code=403, detail="Not a super user")

# Define a function to get the current active user (for token refresh)
def get_current_active_user(db: SessionLocal = Depends(session), token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        token_data = TokenData(username=payload.get("sub"))
        user = crud_user.get_userByUsername(db, token_data.username)
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        raise HTTPException(status_code=401, detail="Login expired")
    return user


# src/services/user.py
import jwt

# Define a function to generate a token
def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


# src/services/user.py
from src.database.database import SessionLocal
from src.crud.crud_user import crud_user

# Define a function to update the user's token
def update_user_token(token: str, refresh_token: str):
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        token_data = TokenData(username=payload.get("sub"))
        user = crud_user.get_userByUsername(SessionLocal(), token_data.username)
        new_token = create_access_token(data={"username": user.username})
        return new_token
    except (jwt.ExpiredSignatureError, jwt.InvalidTokenError):
        raise HTTPException(status_code=401, detail="Invalid token")

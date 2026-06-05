python
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from bcrypt import hashpw, gensalt, checkpw
from datetime import datetime, timedelta
from jose import jwt
from src.db import get_db

router = APIRouter(prefix="/auth", tags=["Authentication"])

ACCESS_TOKEN_EXPIRES_IN = 30 * 60
SECRET_KEY = "SECRET_KEY_HERE"
ALGORITHM = "HS256"

engine = create_engine("sqlite:///database.db")
SessionLocal = sessionmaker(bind=engine)

class User(BaseModel):
    username: str
    email: str
    password: str

    class Config:
        orm_mode = True

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(db: SessionLocal, token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        user = db.query(User).filter(User.username == username).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token has expired")
    except jwt.JWTClaimsError:
        raise HTTPException(status_code=401, detail="Invalid token claims")
    except Exception:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not checkpw(form_data.password.encode("utf-8"), user.password.encode("utf-8")):
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token_expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRES_IN)
    access_token = jwt.encode({"sub": user.username, "exp": access_token_expires}, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": access_token, "token_type": "bearer"}

@router.get("/logout")
async def logout():
    return {"message": "Logged out successfully"}

@router.post("/register")
async def register(user: User, db: session = Depends(get_db)):
    user.password = hashpw(user.password.encode("utf-8"), gensalt())
    db.add(user)
    db.commit()
    return {"message": "User registered successfully"}

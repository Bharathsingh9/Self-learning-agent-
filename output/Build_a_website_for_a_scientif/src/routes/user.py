python
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from src import crud, models, schemas
from src.database import get_db
from src.config import get_settings

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@router.post("/token", response_model=schemas.Token)
async def login_for_access_token(db: Session = Depends(get_db)):
    form_data = OAuth2PasswordRequestForm(None, None)
    user = crud.get_user(db, username=form_data.username)
    if not user or not user.is_active:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = crud.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@router.post("/users/", response_model=schemas.User)
async def create_user(db: Session = Depends(get_db), user: schemas.UserCreate = Depends()):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    try:
        crud.create_user(db, obj_in=user)
    except IntegrityError:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to create user")
    return user

@router.get("/users/me/")
async def read_user_me(db: Session = Depends(get_db), current_user: models.User = Depends()):
    return current_user

@router.get("/users/{user_id}")
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, id=user_id)
    if db_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user


# models.py
from sqlalchemy import ForeignKey, Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)

    # Relationships
    calculations = relationship("Calculation", back_populates="user")



# schemas.py
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    is_active: bool

class Token(BaseModel):
    access_token: str
    token_type: str



# crud.py
from src import models
from src.database import get_db

def get_user(db: Session, username: str):
    return db.query(models.User).filter(models.User.email == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, obj_in: models.UserCreate):
    db_user = models.User(email=obj_in.email, hashed_password=obj_in.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def create_access_token(data: dict):
    # implementation for creating access token
    pass



# database.py
from typing import Dict, Any
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from src.config import get_settings

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = scoped_session(sessionmaker(class_=scoped_session))
        db.configure(bind=create_engine(get_settings().DATABASE_URL))
        setattr(g, '_database', db)
    return db



# config.py
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    SECRET_KEY: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    ALGORITHM: str
    TOKEN_URL: str

    class Config:
        env_file = ".env"

settings = Settings()



# .env
DATABASE_URL=postgresql+psycopg2://user:password@localhost:5432/database
SECRET_KEY=secret_key_here
ACCESS_TOKEN_EXPIRE_MINUTES=60
ALGORITHM=HS256
TOKEN_URL=/token

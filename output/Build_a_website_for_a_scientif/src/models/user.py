python
from passlib.context import CryptContext
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from src.database import database

class User(BaseModel):
    id: int
    username: str
    password: str
    role: str

class UserDB(User):
    class Config:
        orm_mode = True

    @property
    def token_expires(self):
        return self.token_expires_date.replace(tzinfo=None)

class UserManager:
    def __init__(self, ctx: CryptContext):
        self.ctx = ctx
        self.users = []
        self.current_user = None

    def __hash__(self):
        return hash(self.id)

    def signup(self, username: str, password: str, role: str):
        user = UserDB(username=username, password=self.ctx.hash(password), role=role)
        database.session.add(user)
        database.session.commit()

    def signin(self, username: str, password: str):
        user = database.session.query(UserDB).filter(UserDB.username == username).first()
        if user and self.ctx.verify(password, user.password):
            self.current_user = user
            return user
        raise Exception('Invalid credentials')

    def signout(self):
        self.current_user = None

class UserModel(declarative_base()):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    role = Column(String(50), nullable=False)
    token_expires_date = Column(DateTime, nullable=True)


You'll need to install required packages (`passlib`, `pydantic` and `sqlalchemy`).

Don't forget to replace `database` with your database session factory and `CryptContext` with a password hashing context. 

You should configure `CryptContext` with the settings that suit your needs (e.g., password hasher, salt size, etc.). 

This example uses a simple token expiration time. In a production environment, you will want a more robust way to handle token expiration and session management.
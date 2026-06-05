python
# database/schemas.py

from sqlalchemy import Column, Integer, String, Float, Date, Time, DateTime, Enum, Boolean, Text
from sqlalchemy.sql import func
from sqlalchemy.ext.declarative import declarative_base
from enum import Enum as SqlEnum
from datetime import datetime
from pydantic import BaseModel
from pydantic.networks import EmailStr

Base = declarative_base()

class CalcHistory(Base):
    __tablename__ = 'calc_histories'
    id = Column(Integer, primary_key=True)
    operation = Column(String)
    num1 = Column(Float)
    num2 = Column(Float)
    result = Column(Float)
    created_at = Column(DateTime, default=func.now())

class CalcOperations(Base):
    __tablename__ = 'calc_operations'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)

class CalcTypes(Base):
    __tablename__ = 'calc_types'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)

class UserModel(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())

class Calculator(BaseModel):
    num1: float
    num2: float
    operation: str

    class Config:
        orm_mode = True

class User(BaseModel):
    id: int
    email: EmailStr

    class Config:
        orm_mode = True


This file includes the database schema for users, calculator operations and user calculator history. It includes the necessary models for the database tables and for the user and calculator data models.
python
from typing import Optional
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from enum import Enum as PyEnum

class UserType(PyEnum):
    guest = 1
    registered = 2
    admin = 3

class CalculationType(PyEnum):
    arithmetic = 1
    algebraic = 2
    geometric = 3

engine = create_engine('sqlite:///scientific_calculator.db')
Session = sessionmaker(bind=engine)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    type = Column(Enum(UserType), nullable=False)

    calculations = relationship('Calculation', backref='user')
    preferences = relationship('Preference', backref='user')

class Preference(Base):
    __tablename__ = 'preferences'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    unit_system = Column(Enum('metric', 'imperial'), nullable=False)
    display_precision = Column(Integer, nullable=False)

class Calculation(Base):
    __tablename__ = 'calculations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    date = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    type = Column(Enum(CalculationType), nullable=False)
    inputs = Column(String, nullable=False)
    result = Column(String, nullable=False)

class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    date = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    previous_result = Column(String, nullable=False)
    new_input = Column(String, nullable=False)
    new_result = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)

Base.metadata.create_all(engine)

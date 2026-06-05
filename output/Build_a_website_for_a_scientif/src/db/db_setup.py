python
# src/db/db_setup.py

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

Base = declarative_base()

engine = create_engine('sqlite:///scientific_calculator_database.db')

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)

class CalculationHistory(Base):
    __tablename__ = 'calculation_history'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    calculation_expression = Column(String(255), nullable=False)
    result = Column(String(255), nullable=False)
    date_calculated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class RecentCalculations(Base):
    __tablename__ = 'recent_calculations'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    calculation_expression = Column(String(255), nullable=False)
    result = Column(String(255), nullable=False)
    date_calculated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class UserPreferences(Base):
    __tablename__ = 'user_preferences'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    preferred_calculation_type = Column(String(255), nullable=False)
    preferred_decimal_places = Column(Integer, nullable=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

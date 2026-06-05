python
# database/db.py

import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker

# Database Configuration
DB_HOST = 'localhost'
DB_NAME = 'scientific_calculator'
DB_USER = 'scientific_calculator_user'
DB_PASSWORD = 'password'

# Create a connection to the PostgreSQL database
engine = create_engine(
    f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Create a base class for declarative class definitions.
Base = declarative_base()

# Create a table to store users
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)

# Create a table to store calculation history
class CalculationHistory(Base):
    __tablename__ = 'calculation_history'
    
    id = Column(Integer, primary_key=True)
    calculation_type = Column(String)
    input1 = Column(Float)
    input2 = Column(Float)
    result = Column(Float)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = Column(String)
    
# Create all tables in the engine
Base.metadata.create_all(engine)

def get_session():
    """Return a session object"""
    return Session()

def get_all_users():
    """Return all users from the users table"""
    session = get_session()
    users = session.query(User).all()
    session.close()
    return users

def get_user_by_username(username):
    """Return a user object by username"""
    session = get_session()
    user = session.query(User).filter_by(username=username).first()
    session.close()
    return user

def add_user(username, email, password):
    """Add a new user to the users table"""
    session = get_session()
    user = User(username=username, email=email, password=password)
    session.add(user)
    session.commit()
    session.close()

def add_calculation_history(calculation_type, input1, input2, result, user_id):
    """Add a new calculation to the calculation history table"""
    session = get_session()
    calculation = CalculationHistory(
        calculation_type=calculation_type, 
        input1=input1, 
        input2=input2, 
        result=result, 
        user_id=user_id
    )
    session.add(calculation)
    session.commit()
    session.close()

def get_calculation_history():
    """Return all calculations from the calculation history table"""
    session = get_session()
    calculations = session.query(CalculationHistory).all()
    session.close()
    return calculations

def get_calculation_history_for_user(user_id):
    """Return all calculations for a user from the calculation history table"""
    session = get_session()
    calculations = session.query(CalculationHistory).filter_by(user_id=user_id).all()
    session.close()
    return calculations


This code establishes a connection to a PostgreSQL database, creates two tables (users and calculation history), and defines several functions to interact with these tables:

*   `get_session`: Returns a session object.
*   `get_all_users`: Returns all users from the users table.
*   `get_user_by_username`: Returns a user object by username.
*   `add_user`: Adds a new user to the users table.
*   `add_calculation_history`: Adds a new calculation to the calculation history table.
*   `get_calculation_history`: Returns all calculations from the calculation history table.
*   `get_calculation_history_for_user`: Returns all calculations for a user from the calculation history table.
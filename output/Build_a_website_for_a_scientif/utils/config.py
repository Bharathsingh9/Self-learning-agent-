python
# utils/config.py

import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from flask_secret_key import SecretKey

# Load environment variables from .env file
load_dotenv()

# Define database configuration
DB_HOST = os.getenv('DB_HOST')
DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_NAME = os.getenv('DB_NAME')

# Create database engine
engine = create_engine(f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}')

# Create base class for models
Base = declarative_base()

# Define User model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)

# Define Equation model
class Equation(Base):
    __tablename__ = 'equations'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    formula = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

# Define Calculation model
class Calculation(Base):
    __tablename__ = 'calculations'
    id = Column(Integer, primary_key=True)
    equation_id = Column(Integer, ForeignKey('equations.id'))
    input_values = Column(String(500), nullable=False)
    result = Column(String(500), nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))

# Create tables in database
Base.metadata.create_all(engine)

# Create a configured "Session" class
Session = sessionmaker(bind=engine)

# Define secret key for security
secret_key = SecretKey(os.getenv('SECRET_KEY'))

# Define allowed origins
allowed_origins = os.getenv('ALLOWED_ORIGINS', 'http://localhost:3000')

# Define allowed domains
allowed_domains = os.getenv('ALLOWED_DOMAINS', 'localhost')


This code sets up a database management system using SQLAlchemy and Flask to store user-created equations, formulas, and calculation history. It also includes security measures such as password hashing and allowed origins and domains. However, note that this code is incomplete without the necessary dependencies and environment variables. Make sure to install the required libraries and set up your environment variables before running this code.
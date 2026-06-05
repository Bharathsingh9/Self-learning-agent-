python
# src/db/history.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime

# Define the database connection string
DATABASE_URL = 'sqlite:///history.db'
# DATABASE_URL = 'postgresql://user:password@host:port/dbname'

# Create a base class for our database models
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    preferences = Column(JSON)

# Define the History model
class History(Base):
    __tablename__ = 'history'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    calculation = Column(JSON)
    timestamp = Column(DateTime, default=datetime.utcnow)

# Create a session maker
Session = sessionmaker()

# Create a session to the database
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)
Session.configure(bind=engine)

# Define a function to add history
def add_history(session, user_id, calculation):
    new_history = History(user_id=user_id, calculation=calculation)
    session.add(new_history)
    session.commit()

# Define a function to get user preferences
def get_preferences(session, user_id):
    user = session.query(User).get(user_id)
    if user:
        return user.preferences
    return None

# Define a function to update user preferences
def update_preferences(session, user_id, preferences):
    user = session.query(User).get(user_id)
    if user:
        user.preferences = preferences
        session.commit()
    else:
        new_user = User(username='default_username', preferences=preferences)
        session.add(new_user)
        session.commit()

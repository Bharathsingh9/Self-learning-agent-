python
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

def create_table(engine):
    Base.metadata.create_all(engine)

class User(Base):
    __tablename__ = 'user_preferences'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String, unique=True)

class Preference(Base):
    __tablename__ = 'calculator_preferences'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_preferences.id'), nullable=False)
    theme = Column(String)
    currency = Column(String)
    history_limit = Column(Integer, default=10)
    user = relationship("User", backref="preferences")

class History(Base):
    __tablename__ = 'calculator_history'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_preferences.id'), nullable=False)
    date = Column(DateTime)
    expression = Column(String)
    result = Column(String)
    user = relationship("User", backref="history")

class HistoryEntry(Base):
    __tablename__ = 'calculator_history_entry'
    id = Column(Integer, primary_key=True)
    history_id = Column(Integer, ForeignKey('calculator_history.id'), nullable=False)
    expression = Column(String)
    result = Column(String)
    history = relationship("History", backref="entries")

class Theme(Base):
    __tablename__ = 'calculator_theme'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    css = Column(String)

class ThemePreference(Base):
    __tablename__ = 'calculator_theme_preferences'
    id = Column(Integer, primary_key=True)
    theme_id = Column(Integer, ForeignKey('calculator_theme.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user_preferences.id'), nullable=False)
    theme = relationship("Theme", backref="preferences")
    user = relationship("User", backref="themes")

class UserSession(Base):
    __tablename__ = 'calculator_user_session'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user_preferences.id'), nullable=False)
    session_id = Column(String)
    session_key = Column(String)
    user = relationship("User", backref="sessions")

class Database:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        create_table(self.engine)
        Base.metadata.reflect(self.engine)

    def session(self):
        return sessionmaker(bind=self.engine)()

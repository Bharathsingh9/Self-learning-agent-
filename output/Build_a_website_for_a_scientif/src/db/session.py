python
# src/db/session.py
from fastapi import FastAPI
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.exc import IntegrityError

SQLALCHEMY_DATABASE_URL = 'sqlite:///scientific_calculator.db'
BASE_DB_SESSION = None

def db_session():
    global BASE_DB_SESSION
    if BASE_DB_SESSION is None:
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
        BASE_DB_SESSION = SessionLocal
        return SessionLocal()
    else:
        return BASE_DB_SESSION

def close_db_connection(session):
    session.close()

from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class History(Base):
    __tablename__ = 'history'
    id = Column(Integer, primary_key=True)
    expression = Column(String, nullable=False)
    result = Column(String, nullable=False)
    timestamp = Column(DateTime, nullable=False)

Base.metadata.create_all(bind=db_session().get_bind())

app = FastAPI()

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    return JSONResponse(
        status_code=422,
        content={"error": "Invalid request"},
    )

@app.on_event("shutdown")
async def database_shutdown_event():
    await db_session().get_bind().dispose()

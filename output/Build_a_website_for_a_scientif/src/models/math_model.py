python
# src/models/math_model.py

from typing import Dict, Literal
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import math

SQLALCHEMY_DATABASE_URL = "sqlite:///math_calculations.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Calculation(Base):
    __tablename__ = "calculations"
    id = Column(Integer, primary_key=True, index=True)
    expression = Column(String)
    result = Column(Float)
    method = Column(String)
    created_at = Column(DateTime, default=datetime.now)

class MathModel(BaseModel):
    expression: str
    method: Literal["ADD", "SUB", "MUL", "DIV"]
    result: float

    def calculate(self):
        try:
            if self.method == "ADD":
                return self.expression.split("+")[0] + self.expression.split("+")[1]
            elif self.method == "SUB":
                return self.expression.split("-")[0] - self.expression.split("-")[1]
            elif self.method == "MUL":
                return math.prod(map(int, self.expression.split("*")))
            elif self.method == "DIV":
                numbers = self.expression.replace("/", " ").split(" ")
                numbers = list(map(int, numbers))
                if numbers[1] != 0:
                    return numbers[0] / numbers[1]
                else:
                    return "Error: Division by zero"
        except Exception as e:
            return str(e)

class Calculator:
    @staticmethod
    def get_last_calculation(db_session: SessionLocal):
        result = db_session.query(Calculation).order_by(Calculation.id.desc()).first()
        return result

    @staticmethod
    def add_calculation(db_session: SessionLocal, expression: str, method: Literal["ADD", "SUB", "MUL", "DIV"], result: float):
        calculation = Calculation(
            expression=expression,
            result=result,
            method=str(method)
        )
        db_session.add(calculation)
        db_session.commit()

    @staticmethod
    def calculate(db_session: SessionLocal, math_model: MathModel):
        result = math_model.calculate()
        db_session.add(calculation=Calculation(expression=math_model.expression, result=float(result), method=math_model.method))
        db_session.commit()
        return result

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

import uvicorn
from fastapi import FastAPI, Depends
from pydantic import BaseModel
import asyncio
import json

app = FastAPI()

@app.get("/last_calculation")
async def last_calculation(db: SessionLocal = Depends(get_db)):
    return Calculator.get_last_calculation(db)

@app.post("/calculate")
async def calculate(db: SessionLocal = Depends(get_db), math_model: MathModel):
    return Calculator.calculate(db, math_model)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

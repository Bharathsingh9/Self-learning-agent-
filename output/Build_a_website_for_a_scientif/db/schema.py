python
# db/schema.py

from datetime import datetime
from typing import Optional

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, Float, DateTime
from sqlalchemy.ext.devolent import DeclarativeBase

class Result(BaseModel):
    id: Optional[int]
    expression: str
    result: float
    created_at: Optional[datetime]

class CalculatorData(DeclarativeBase):
    __tablename__ = 'calculations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    expression = Column(String, nullable=False)
    result = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.now)

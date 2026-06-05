python
# models/formula.py

from datetime import datetime
from typing import List
from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db import Base

class CalculationMethod(Base):
    __tablename__ = 'calculation_methods'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True)
    description = Column(Text)

class Formula(Base):
    __tablename__ = 'formulas'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), unique=True)
    description = Column(Text)
    calculation_method_id = Column(Integer, ForeignKey('calculation_methods.id'))
    calculation_method = relationship('CalculationMethod', backref='formulas')
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.current_timestamp())

class Calculation(Base):
    __tablename__ = 'calculations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    formula_id = Column(Integer, ForeignKey('formulas.id'))
    formula = relationship('Formula', backref='calculations')
    input_values = Column(Text)
    result = Column(Text)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.current_timestamp())

class CalculationError(Base):
    __tablename__ = 'calculation_errors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    calculation_id = Column(Integer, ForeignKey('calculations.id'))
    calculation = relationship('Calculation', backref='calculation_errors')
    error_message = Column(Text)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.current_timestamp())

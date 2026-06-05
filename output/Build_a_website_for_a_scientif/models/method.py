python
# models/method.py

from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

Base = declarative_base()

class FormulaMethod(Base):
    __tablename__ = 'formula_methods'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=True)
    description = Column(Text)

class Formula(Base):
    __tablename__ = 'formulas'

    id = Column(Integer, primary_key=True)
    formula_method_id = Column(Integer, ForeignKey('formula_methods.id'))
    formula_method = relationship('FormulaMethod', backref='formulas')
    expression = Column(Text)
    type = Column(String(50))

class CalculationHistory(Base):
    __tablename__ = 'calculation_histories'

    id = Column(Integer, primary_key=True)
    formula_id = Column(Integer, ForeignKey('formulas.id'))
    formula = relationship('Formula', backref='calculation_histories')
    input_data = Column(Text)
    result = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

class CalculationResult(Base):
    __tablename__ = 'calculation_results'

    id = Column(Integer, primary_key=True)
    calculation_history_id = Column(Integer, ForeignKey('calculation_histories.id'))
    calculation_history = relationship('CalculationHistory', backref='calculation_results')
    result_details = Column(Text)
    status = Column(String(20))

engine = create_engine('sqlite:///scientific_calculator.db') # SQLite database for local development
Base.metadata.create_all(engine)

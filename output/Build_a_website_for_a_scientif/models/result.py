python
# File: models/result.py

from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class CalculationMethod(BaseModel):
    id: int
    method_name: str
    description: str

class Formula(BaseModel):
    id: int
    calculation_method_id: int
    formula_name: str
    formula_expression: str
    description: str
    calculation_method: CalculationMethod

class CalculationResult(BaseModel):
    id: int
    formula_id: int
    input_values: str
    result: str
    timestamp: datetime
    result_description: Optional[str]

class CalculationResultWithFormula(BaseModel):
    id: int
    formula: Formula
    input_values: str
    result: str
    timestamp: datetime
    result_description: Optional[str]

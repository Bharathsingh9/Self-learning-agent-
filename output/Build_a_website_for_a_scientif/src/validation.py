python
# src/validation.py

import re
from typing import Dict, Any

class Validation:
    def __init__(self, data: Dict[str, Any]):
        self.data = data

    def validate_input(self) -> bool:
        if not self.data:
            raise ValueError("Input data cannot be empty")
        
        for key, value in self.data.items():
            if key not in ['num1', 'num2', 'operator', 'num3']:
                raise ValueError(f"Invalid key: {key}")
            
            if key == 'num1' and not self.validate_number_value(value):
                raise ValueError(f"Invalid number for {key}")
            
            if key == 'operator' and not self.validate_operator(value):
                raise ValueError(f"Invalid operator: {value}")
            
            if key == 'num3' and not self.validate_number_value(value):
                raise ValueError(f"Invalid number for {key}")

        return True

    @staticmethod
    def validate_number_value(value: str) -> bool:
        if not re.match(r"^\d+(\.\d+)?$", value):
            return False
        return True

    @staticmethod
    def validate_operator(value: str) -> bool:
        for operator in ['+', '-', '*', '/']:
            if operator == value:
                return True
        
        return False

class ErrorHandling:
    @staticmethod
    def handle_division_by_zero() -> bool:
        print("Error: Division by zero is not allowed.")
        return False

    @staticmethod
    def handle_invalid_operator() -> bool:
        print("Error: Invalid operator. Please use '+', '-', '*' or '/'.")
        return False

    @staticmethod
    def handle_invalid_input() -> bool:
        print("Error: Invalid input. Please enter numbers and a valid operator.")
        return False

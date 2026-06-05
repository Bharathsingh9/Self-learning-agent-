python
from datetime import datetime
from typing import Union
from src.models.users import UserDB

class Calculation:
    def __init__(self, user: UserDB):
        self.user = user
        self.history = []

    def store_calculation(self, calculation: dict) -> None:
        calculation['created_at'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.history.append(calculation)
        self.user.calculation_history = self.history

    def execute_operation(self, operation: str, *args: Union[int, float]) -> dict:
        try:
            if operation == 'add':
                result = sum(args)
                return {'operation': 'add', 'result': result, 'operands': args}
            elif operation == 'subtract':
                result = args[0] - args[1]
                return {'operation': 'subtract', 'result': result, 'operands': args}
            elif operation == 'multiply':
                result = 1
                for arg in args:
                    result *= arg
                return {'operation': 'multiply', 'result': result, 'operands': args}
            elif operation == 'divide':
                if args[1] == 0:
                    return {'error': 'Divide by zero'}
                result = args[0] / args[1]
                return {'operation': 'divide', 'result': result, 'operands': args}
            else:
                return {'error': 'Invalid operation'}
        except Exception as e:
            return {'error': str(e)}

    def calculate(self, equation: str) -> dict:
        try:
            parts = equation.split('=')
            if len(parts) != 2:
                raise Exception('Invalid equation format')
            result, history = self.parse_equation(equation)
            return result
        except Exception as e:
            return {'error': str(e)}

    def parse_equation(self, equation: str) -> tuple:
        stack = []
        for char in equation:
            if char == '+':
                b, a = next(iter(stack)), stack.pop(0)
                stack = [a + b] + stack
            elif char == '-':
                b, a = next(iter(stack)), stack.pop(0)
                stack = [a - b] + stack
            elif char == '*':
                b, a = next(iter(stack)), stack.pop(0)
                stack = [a * b] + stack
            elif char == '/':
                b, a = next(iter(stack)), stack.pop(0)
                if b == 0:
                    raise Exception('Division by zero')
                stack = [a / b] + stack
            else:
                stack.insert(0, int(char))
        return {'result': stack[0]}, equation

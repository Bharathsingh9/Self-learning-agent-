python
# src/utils.py
import json
import sqlite3
from decimal import Decimal, getcontext

# Define a function to connect to the SQLite database
def connect_database(db_name):
    try:
        conn = sqlite3.connect(db_name)
        return conn
    except sqlite3.Error as e:
        print(f"Error connecting to database: {e}")
        return False

# Define a function to create a new table in the database
def create_table(conn, table_name, columns):
    try:
        c = conn.cursor()
        column_str = ', '.join([f"{col[0]} {col[1]}" for col in columns])
        query = f"CREATE TABLE IF NOT EXISTS {table_name} ({column_str})"
        c.execute(query)
        conn.commit()
    except sqlite3.Error as e:
        print(f"Error creating table: {e}")

# Define a function to perform mathematical calculations
class Calculator:
    def __init__(self):
        self.math_operations = {
            '+': self.add,
            '-': self.subtract,
            '*': self.multiply,
            '/': self.divide,
            '**': self.exponent,
            '^': self.power,
            '%': self.modulus,
            'sqrt': self.square_root,
            'sin': self.sin,
            'cos': self.cos,
            'tan': self.tan,
            'log': self.log,
            'exp': self.exp,
            'ceil': self.ceil,
            'floor': self.floor
        }

    def add(self, a, b):
        return str(a + b)

    def subtract(self, a, b):
        return str(a - b)

    def multiply(self, a, b):
        return str(a * b)

    def divide(self, a, b):
        try:
            return str(Decimal(a) / Decimal(b))
        except ZeroDivisionError:
            return "Error: Division by zero"

    def exponent(self, a, b):
        try:
            return str(Decimal(a) ** Decimal(b))
        except ValueError:
            return "Error: Invalid exponent"

    def power(self, a, b):
        try:
            return str(Decimal(a) ** Decimal(b))
        except TypeError:
            return "Error: Invalid operation"

    def modulus(self, a, b):
        try:
            return str(int(Decimal(a)) % int(Decimal(b)))
        except ZeroDivisionError:
            return "Error: Division by zero"

    def square_root(self, a):
        try:
            return str(Decimal(a).sqrt())
        except TypeError:
            return "Error: Invalid operation"

    def sin(self, a):
        try:
            getcontext().prec = 28
            sin_a = Decimal(a).sin()
            return str(sin_a)
        except TypeError:
            return "Error: Invalid operation"

    def cos(self, a):
        try:
            getcontext().prec = 28
            cos_a = Decimal(a).cos()
            return str(cos_a)
        except TypeError:
            return "Error: Invalid operation"

    def tan(self, a):
        try:
            getcontext().prec = 28
            tan_a = Decimal(a).tan()
            return str(tan_a)
        except TypeError:
            return "Error: Invalid operation"

    def log(self, a):
        try:
            return str(Decimal(a).log10())
        except TypeError:
            return "Error: Invalid operation (log10)"

    def exp(self, a):
        try:
            getcontext().prec = 28
            exp_a = Decimal(a).exp()
            return str(exp_a)
        except TypeError:
            return "Error: Invalid operation"

    def ceil(self, a):
        try:
            return str(Decimal(a).to_integral_value(rounding="CEILING"))
        except TypeError:
            return "Error: Invalid operation"

    def floor(self, a):
        try:
            return str(Decimal(a).to_integral_value(rounding="FLOOR"))
        except TypeError:
            return "Error: Invalid operation"

    def calculate(self, expression):
        for operation in self.math_operations:
            if operation in expression:
                operation_name, operand1, operand2 = expression.split(operation, 1)
                operand1 = self.calculate(operand1.strip()) if operand1 not in self.math_operations else self.math_operations[operand1](operand1)
                operand2 = self.calculate(operand2.strip()) if operand2 not in self.math_operations else self.math_operations[operand2](operand2)
                return self.math_operations[operation](operand1, operand2)
        try:
            return str(Decimal(expression))
        except ValueError:
            return "Error: Invalid calculation"

# Define a function to perform calculations
def calculate(expression, table_name, db_name):
    calculator = Calculator()
    conn = connect_database(db_name)
    if conn:
        create_table(conn, table_name, [("expression", "text"), ("result", "text")])
        result = calculator.calculate(expression)
        c = conn.cursor()
        query = f"INSERT INTO {table_name} (expression, result) VALUES (?, ?)"
        c.execute(query, (expression, result))
        conn.commit()
        return result
    else:
        return "Error: Failed to connect to database"

# Define a function to get results from the database
def get_results(table_name, db_name):
    conn = connect_database(db_name)
    if conn:
        c = conn.cursor()
        query = f"SELECT * FROM {table_name}"
        c.execute(query)
        results = c.fetchall()
        return [json.dumps(result) for result in results]
    else:
        return ["Error: Failed to connect to database"]

# Define a function to delete a record from the database
def delete_record(table_name, id, db_name):
    conn = connect_database(db_name)
    if conn:
        c = conn.cursor()
        query = f"DELETE FROM {table_name} WHERE id=?"
        c.execute(query, (id,))
        conn.commit()
        return "Record deleted successfully"
    else:
        return "Error: Failed to connect to database"

# Define a function to get a record from the database
def get_record(table_name, id, db_name):
    conn = connect_database(db_name)
    if conn:
        c = conn.cursor()
        query = f"SELECT * FROM {table_name} WHERE id=?"
        c.execute(query, (id,))
        result = c.fetchone()
        if result:
            return json.dumps(result)
        else:
            return "Error: Record not found"
    else:
        return "Error: Failed to connect to database"

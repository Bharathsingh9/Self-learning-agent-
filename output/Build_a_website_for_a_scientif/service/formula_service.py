python
import sqlite3

class FormulaService:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS formulas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                formula TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS calculation_methods (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                method TEXT NOT NULL,
                formula_id INTEGER NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (formula_id) REFERENCES formulas (id)
            );
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                calculation_method_id INTEGER NOT NULL,
                input_values TEXT NOT NULL,
                result TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (calculation_method_id) REFERENCES calculation_methods (id)
            );
        ''')

        self.conn.commit()

    def add_formula(self, name, description, formula):
        self.cursor.execute('''
            INSERT INTO formulas (name, description, formula)
            VALUES (?, ?, ?);
        ''', (name, description, formula))
        formula_id = self.cursor.lastrowid
        self.conn.commit()
        return formula_id

    def add_calculation_method(self, name, description, method, formula_id):
        self.cursor.execute('''
            INSERT INTO calculation_methods (name, description, method, formula_id)
            VALUES (?, ?, ?, ?);
        ''', (name, description, method, formula_id))
        calculation_method_id = self.cursor.lastrowid
        self.conn.commit()
        return calculation_method_id

    def add_result(self, calculation_method_id, input_values, result):
        self.cursor.execute('''
            INSERT INTO results (calculation_method_id, input_values, result)
            VALUES (?, ?, ?);
        ''', (calculation_method_id, input_values, result))
        result_id = self.cursor.lastrowid
        self.conn.commit()
        return result_id

    def get_formula_by_id(self, formula_id):
        self.cursor.execute('''
            SELECT * FROM formulas
            WHERE id = ?;
        ''', (formula_id,))
        formulas = self.cursor.fetchone()
        return formulas

    def get_calculation_methods_by_formula_id(self, formula_id):
        self.cursor.execute('''
            SELECT * FROM calculation_methods
            WHERE formula_id = ?;
        ''', (formula_id,))
        methods = self.cursor.fetchall()
        return methods

    def get_results_by_calculation_method_id(self, calculation_method_id):
        self.cursor.execute('''
            SELECT * FROM results
            WHERE calculation_method_id = ?;
        ''', (calculation_method_id,))
        results = self.cursor.fetchall()
        return results

    def close(self):
        self.conn.close()


Example usage:


# create a FormulaService instance
formula_service = FormulaService('scientific_calculator.db')

# add a formula
formula_id = formula_service.add_formula(
    'Formula Example',
    'This is a formula example',
    'a + b'
)

# add a calculation method for the formula
calculation_method_id = formula_service.add_calculation_method(
    'Addition Method',
    'This is an addition method',
    'return a + b',
    formula_id
)

# add a result for the calculation method
result_id = formula_service.add_result(
    calculation_method_id,
    '{"a": 1, "b": 2}',
    '3'
)

# get the formula
formula = formula_service.get_formula_by_id(formula_id)
print(formula)

# get the calculation methods
methods = formula_service.get_calculation_methods_by_formula_id(formula_id)
print(methods)

# get the results
results = formula_service.get_results_by_calculation_method_id(calculation_method_id)
print(results)

# close the FormulaService instance
formula_service.close()

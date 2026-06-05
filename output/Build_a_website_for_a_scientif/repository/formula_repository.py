python
import sqlite3
from sqlite3 import Error

class FormulaRepository:
    def __init__(self, db_name="scientific_calculator.db"):
        self.conn = self.create_connection(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_connection(self, db_name):
        try:
            conn = sqlite3.connect(db_name)
            return conn
        except Error as e:
            print(e)
            return None

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS formulas
            (id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            description TEXT,
            formula TEXT NOT NULL)
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS calculation_methods
            (id INTEGER PRIMARY KEY,
            formula_id INTEGER,
            method TEXT NOT NULL,
            method_description TEXT,
            FOREIGN KEY (formula_id) REFERENCES formulas(id))
        ''')

        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS results
            (id INTEGER PRIMARY KEY,
            calculation_method_id INTEGER,
            value REAL NOT NULL,
            FOREIGN KEY (calculation_method_id) REFERENCES calculation_methods(id))
        ''')

        self.conn.commit()

    def insert_formula(self, name, description, formula):
        self.cursor.execute('INSERT INTO formulas (name, description, formula) VALUES (?, ?, ?)', (name, description, formula))
        self.conn.commit()
        return self.cursor.lastrowid

    def insert_calculation_method(self, formula_id, method, method_description):
        self.cursor.execute('INSERT INTO calculation_methods (formula_id, method, method_description) VALUES (?, ?, ?)', (formula_id, method, method_description))
        self.conn.commit()
        return self.cursor.lastrowid

    def insert_result(self, calculation_method_id, value):
        self.cursor.execute('INSERT INTO results (calculation_method_id, value) VALUES (?, ?)', (calculation_method_id, value))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_formula(self, id):
        self.cursor.execute('SELECT * FROM formulas WHERE id=?', (id,))
        return self.cursor.fetchone()

    def get_formulas(self):
        self.cursor.execute('SELECT * FROM formulas')
        return self.cursor.fetchall()

    def get_calculation_methods(self, formula_id):
        self.cursor.execute('SELECT * FROM calculation_methods WHERE formula_id=?', (formula_id,))
        return self.cursor.fetchall()

    def get_results(self, calculation_method_id):
        self.cursor.execute('SELECT * FROM results WHERE calculation_method_id=?', (calculation_method_id,))
        return self.cursor.fetchall()

    def close_connection(self):
        if (self.conn):
            self.conn.close()


Note: This is a very basic implementation, and you might need to adapt it to your specific requirements.
python
# repository/result_repository.py

import sqlite3
from sqlite3 import Error

class ResultRepository:
    def __init__(self, db_file):
        self.conn = None
        try:
            self.conn = sqlite3.connect(db_file)
            print(sqlite3.version)
        except Error as e:
            print(e)
        self.cursor = self.conn.cursor()

        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS formulas (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                description TEXT
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS calculation_methods (
                id INTEGER PRIMARY KEY,
                formula_id INTEGER NOT NULL,
                method TEXT NOT NULL,
                formula TEXT NOT NULL,
                FOREIGN KEY (formula_id) REFERENCES formulas (id)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS results (
                id INTEGER PRIMARY KEY,
                calculation_method_id INTEGER NOT NULL,
                input1 REAL NOT NULL,
                input2 REAL NOT NULL,
                result REAL NOT NULL,
                FOREIGN KEY (calculation_method_id) REFERENCES calculation_methods (id)
            )
        """)
        self.conn.commit()

    def save_formula(self, name, description):
        self.cursor.execute("INSERT INTO formulas (name, description) VALUES (?, ?)", (name, description))
        self.conn.commit()

    def save_calculation_method(self, formula_id, method, formula):
        self.cursor.execute("INSERT INTO calculation_methods (formula_id, method, formula) VALUES (?, ?, ?)", (formula_id, method, formula))
        self.conn.commit()
        return self.cursor.lastrowid

    def save_result(self, calculation_method_id, input1, input2, result):
        self.cursor.execute("INSERT INTO results (calculation_method_id, input1, input2, result) VALUES (?, ?, ?, ?)", (calculation_method_id, input1, input2, result))
        self.conn.commit()
        return self.cursor.lastrowid

    def get_formula(self, id):
        self.cursor.execute("SELECT * FROM formulas WHERE id = ?", (id,))
        return self.cursor.fetchone()

    def get_formula_by_name(self, name):
        self.cursor.execute("SELECT * FROM formulas WHERE name = ?", (name,))
        return self.cursor.fetchone()

    def get_calculation_methods(self, formula_id=None):
        if formula_id:
            self.cursor.execute("SELECT * FROM calculation_methods WHERE formula_id = ?", (formula_id,))
        else:
            self.cursor.execute("SELECT * FROM calculation_methods")
        return self.cursor.fetchall()

    def get_results(self, calculation_method_id=None):
        if calculation_method_id:
            self.cursor.execute("SELECT * FROM results WHERE calculation_method_id = ?", (calculation_method_id,))
        else:
            self.cursor.execute("SELECT * FROM results")
        return self.cursor.fetchall()

    def close_connection(self):
        if self.conn:
            self.conn.close()


This code will create a SQLite database file and set up three tables: `formulas`, `calculation_methods`, and `results`. It provides methods for inserting, retrieving, and closing the database connection.
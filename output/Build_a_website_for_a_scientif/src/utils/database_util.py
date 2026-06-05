python
# src/utils/database_util.py

import sqlite3
from sqlite3 import Error

# Set database configuration
DB_NAME = 'scientific_calculator.db'
TABLE_NAME = 'calculations'

# Create a connection to the SQLite database
def create_connection():
    conn = None
    try:
        conn = sqlite3.connect(DB_NAME)
        return conn
    except Error as e:
        print(e)

# Create table if it doesn't exist
def create_table(conn):
    sql = '''CREATE TABLE IF NOT EXISTS %s (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                operation TEXT NOT NULL,
                num1 REAL NOT NULL,
                num2 REAL NOT NULL,
                result REAL NOT NULL,
                created_at TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
            );''' % TABLE_NAME
    try:
        cur = conn.cursor()
        cur.execute(sql)
    except Error as e:
        print(e)

# Insert calculation data into the database
def insert_calculation(conn, calculation):
    sql = '''INSERT INTO %s (
                operation, num1, num2, result
            ) VALUES (?, ?, ?, ?);''' % TABLE_NAME
    try:
        cur = conn.cursor()
        cur.execute(sql, (calculation['operation'], calculation['num1'], calculation['num2'], calculation['result']))
        conn.commit()
        return cur.lastrowid
    except Error as e:
        print(e)
        return None

# Fetch all calculation data from the database
def get_all_calculations(conn):
    sql = '''SELECT * FROM %s;''' % TABLE_NAME
    try:
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        return rows
    except Error as e:
        print(e)
        return None

# Fetch calculation data by id from the database
def get_calculation_by_id(conn, id):
    sql = '''SELECT * FROM %s WHERE id = ?;''' % TABLE_NAME
    try:
        cur = conn.cursor()
        cur.execute(sql, (id,))
        row = cur.fetchone()
        return row
    except Error as e:
        print(e)
        return None

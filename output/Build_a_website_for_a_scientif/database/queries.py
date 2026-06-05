python
# database/queries.py

import sqlite3
from sqlite3 import Error
import hashlib
import jwt
import datetime

# database connection settings
DB_FILE = 'sci_calculator.db'

# create a new user
def create_user(username, password):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        query = "INSERT INTO users (username, password_hash, created_at, updated_at) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (username, hashlib.sha256(password.encode('utf-8')).hexdigest(), datetime.datetime.now(), datetime.datetime.now()))
        conn.commit()
        conn.close()
        return True
    except Error as e:
        print(e)
        return False

# create an equation
def create_equation(username, equation):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        query = "INSERT INTO equations (username, equation, created_at, updated_at) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (username, equation, datetime.datetime.now(), datetime.datetime.now()))
        conn.commit()
        conn.close()
        return True
    except Error as e:
        print(e)
        return False

# get all equations for a user
def get_equations(username):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        query = "SELECT id, equation, created_at, updated_at FROM equations WHERE username = ? ORDER BY created_at DESC"
        cursor.execute(query, (username,))
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Error as e:
        print(e)
        return []

# get an equation by id
def get_equation(equation_id, username):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        query = "SELECT id, equation, created_at, updated_at FROM equations WHERE id = ? AND username = ?"
        cursor.execute(query, (equation_id, username))
        row = cursor.fetchone()
        conn.close()
        return row
    except Error as e:
        print(e)
        return None

# delete an equation
def delete_equation(equation_id, username):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        query = "DELETE FROM equations WHERE id = ? AND username = ?"
        cursor.execute(query, (equation_id, username))
        conn.commit()
        conn.close()
        return True
    except Error as e:
        print(e)
        return False

# get calculation history
def get_calculation_history(username):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        query = "SELECT id, equation, result, created_at, updated_at FROM calculations WHERE username = ? ORDER BY created_at DESC"
        cursor.execute(query, (username,))
        rows = cursor.fetchall()
        conn.close()
        return rows
    except Error as e:
        print(e)
        return []

# calculate result for an equation
def calculate_result(username, equation):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        query = "INSERT INTO calculations (username, equation, result, created_at, updated_at) VALUES (?, ?, ?, ?, ?)"
        result = eval(equation)  # WARNING: Evaluating user input directly can be a security risk if equation is coming from a user. Use a safer library or method for evaluating equations.
        cursor.execute(query, (username, equation, result, datetime.datetime.now(), datetime.datetime.now()))
        conn.commit()
        conn.close()
        return result
    except Exception as e:
        print(e)
        return None

# verify user credentials
def verify_user_credentials(username, password):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        query = "SELECT password_hash FROM users WHERE username = ?"
        cursor.execute(query, (username,))
        row = cursor.fetchone()
        if row and row[0] == hashlib.sha256(password.encode('utf-8')).hexdigest():
            return True
        conn.close()
        return False
    except Error as e:
        print(e)
        return False

# generate JWT token for user
def generate_jwt_token(username):
    try:
        payload = {'username': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}
        token = jwt.encode(payload, secret_key='your_secret_key', algorithm='HS256')
        return token
    except Exception as e:
        print(e)
        return None

# decode JWT token for user
def decode_jwt_token(token):
    try:
        payload = jwt.decode(token, secret_key='your_secret_key', algorithms=['HS256'])
        return payload['username']
    except Exception as e:
        print(e)
        return None

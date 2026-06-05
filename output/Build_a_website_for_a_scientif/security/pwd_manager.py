python
# security/pwd_manager.py

import sqlite3
import os
import hashlib
import secrets

class PwdManager:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS equations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                equation TEXT NOT NULL,
                formula TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS calculation_history (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                calculation TEXT NOT NULL,
                timestamp TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (user_id)
            )
        ''')
        self.conn.commit()

    def add_user(self, username, password):
        salt = secrets.token_hex(16)
        hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
        self.cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password + salt))
        self.conn.commit()

    def check_user_credentials(self, username, password):
        self.cursor.execute('SELECT password FROM users WHERE username = ?', (username,))
        stored_hash = self.cursor.fetchone()
        if stored_hash:
            stored_hash, salt = stored_hash[0], stored_hash[:32]
            hashed_password = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt.encode('utf-8'), 100000)
            return hashed_password == stored_hash
        return False

    def add_equation(self, user_id, equation, formula):
        self.cursor.execute('INSERT INTO equations (user_id, equation, formula, timestamp) VALUES (?, ?, ?, datetime())',
                            (user_id, equation, formula))
        self.conn.commit()

    def get_equations(self, user_id):
        self.cursor.execute('SELECT equation, formula FROM equations WHERE user_id = ?', (user_id,))
        return self.cursor.fetchall()

    def add_calculation_history(self, user_id, calculation):
        self.cursor.execute('INSERT INTO calculation_history (user_id, calculation, timestamp) VALUES (?, ?, datetime())',
                            (user_id, calculation))
        self.conn.commit()

    def get_calculation_history(self, user_id):
        self.cursor.execute('SELECT calculation FROM calculation_history WHERE user_id = ?', (user_id,))
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()

Note: Please modify the file path in `PwdManager` class as per your actual file path and requirements.
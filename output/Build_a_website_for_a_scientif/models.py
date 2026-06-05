python
# models.py

from datetime import datetime
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
import secrets

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    calculations = db.relationship('Calculation', backref='user', lazy=True)

    def set_password(self, password):
        self.password = PasswordManager.hash_password(password)

    def check_password(self, password):
        return PasswordManager.check_password(password, self.password)


class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equation = db.Column(db.Text, nullable=False)
    result = db.Column(db.Float, nullable=False)
    history = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


class PasswordManager:
    @staticmethod
    def hash_password(password):
        salt = secrets.token_hex(16)
        return f"{PasswordManager._hash(password)}.{salt}"

    @staticmethod
    def _hash(password):
        import hashlib
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def check_password(password, hashed_password):
        if isinstance(hashed_password, str) and '.' in hashed_password:
            hashed, salt = hashed_password.split('.')
            return PasswordManager._hash(password) == hashed and salt == secrets.token_hex(16)
        elif isinstance(hashed_password, str):
            return PasswordManager._hash(password) == hashed_password


**Note**: The `PasswordManager` class uses a simple SHA-256 hashing mechanism with a randomly generated salt. However, for a production-grade application, consider using a more robust hashing algorithm like bcrypt or Argon2, and a library like `Flask-Bcrypt` for secure password storage.
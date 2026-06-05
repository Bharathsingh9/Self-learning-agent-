python
# src/models.py
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import datetime

db = SQLAlchemy()

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    calculated_values = db.relationship('CalculatedValues', backref='user', lazy=True)

class CalculatedValues(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    operation = db.Column(db.String(10), nullable=False)
    number1 = db.Column(db.Numeric(10, 2), nullable=False)
    number2 = db.Column(db.Numeric(10, 2), nullable=False)
    result = db.Column(db.Numeric(10, 2), nullable=False)
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.datetime.utcnow)

    def __repr__(self):
        return f'<CalculatedValues {self.id} {self.operation} {self.number1} {self.number2} {self.result} {self.date_created}>'

class Operations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    operation_name = db.Column(db.String(20), unique=True, nullable=False)
    operation_description = db.Column(db.String(200), nullable=True)

class Formula(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    formula_name = db.Column(db.String(50), unique=True, nullable=False)
    formula_description = db.Column(db.String(200), nullable=True)
    formula_expression = db.Column(db.String(200), nullable=False)
    formula_result = db.Column(db.Numeric(10, 2), nullable=False)
    operation_id = db.Column(db.Integer, db.ForeignKey('operations.id'), nullable=True)

This code defines four models: User, CalculatedValues, Operations, and Formula. Each model is designed to store specific information. The User model stores the information for registered users. The CalculatedValues model stores the calculated results for each user. The Operations model stores the different mathematical operations supported by the calculator. The Formula model stores different mathematical formulas.
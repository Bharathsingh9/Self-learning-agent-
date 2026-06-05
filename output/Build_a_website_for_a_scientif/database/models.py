python
# database/models.py

from flask_sqlalchemy import SQLAlchemy
import json

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class CalculatorHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    history = db.Column(db.String(200), nullable=False)

    def __repr__(self):
        return f'<CalculatorHistory {self.history}>'

class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    expression = db.Column(db.String(100), nullable=False)
    result = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Calculation {self.expression}: {self.result}>'

class CalculatorSetting(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    setting = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<CalculatorSetting {self.setting}>'


And database configuration in `__init__.py` file:


# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    db.init_app(app)

    app.app_context().push()

    return app

engine = create_engine('sqlite:///database.db')
db.metadata.create_all(engine)

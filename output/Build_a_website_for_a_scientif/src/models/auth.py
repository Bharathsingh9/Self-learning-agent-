python
# src/models/auth.py

from flask import Flask, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, LoginManager
from flask_user import UserMixin, UserManager, SQLAlchemyAdapter, SQLAlchemyBaseQuery
from src import login_manager
from src import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.name}')"

    def __init__(self, id, name, username, password):
        self.id = id
        self.name = name
        self.username = username
        self.password = generate_password_hash(password)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class AnonymousUser(UserMixin):
    id = -1
    username = "Anonymous"
    name = ""

class UserMixin(UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    is_admin = db.Column(db.Boolean, default=False, nullable=False)

class AuthManager:
    def __init__(self, app):
        self.app = app

    def authenticate(self, username, password):
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):
            return user

    def authorize(self, user, resource="calculator"):
        if user.is_admin or (resource == "calculator" and user.is_admin == False):
            return True


class UserLoginManager:
    def __init__(self, app, User, UserMixin, auth_manager):
        self.app = app
        self.login_manager = login_manager
        self.User = User
        self.UserMixin = UserMixin

    def init_app(self):
        db.create_all()

        self.login_manager = LoginManager()
        self.login_manager.init_app(self.app)
        self.login_manager.login_view = "login"
        self.login_manager.login_message_category = "info"

        self.user_adapter = SQLAlchemyAdapter(self.User, self.UserMixin)

        self.login_manager.login_manager.user_query = self.user_adapter.get_user
        self.login_manager.login_manager.session_protection = None
        self.login_manager.login_manager.session_protection_domain = None

        self.user_manager = UserManager(
            self.user_adapter,
            self.app,
            property_loader=lambda u: self.user_adapter.load_user(u.id),
        )

        @self.app.route("/login")
        def login():
            return "Logged in successfully"

        @self.app.route("/logout")
        def logout():
            return "Logged out successfully"

user_manager = UserLoginManager(db.app, User, UserMixin, AuthManager(db.app))
user_manager.init_app()

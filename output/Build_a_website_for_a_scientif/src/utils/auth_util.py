python
# src/utils/auth_util.py

import jwt
from src.config import secret_key
from src.models.user import User
from src.db.database import db
from flask import current_app
from datetime import datetime, timedelta

def generate_access_token(user_id):
    try:
        payload = {'exp': datetime.utcnow() + timedelta(hours=1), 'iat': datetime.utcnow(), 'sub': user_id}
        access_token = jwt.encode(payload, secret_key, algorithm='HS256')
        return access_token
    except Exception as e:
        current_app.logger.error(f'Failed to generate access token: {e}')
        return None

def verify_access_token(token):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        user = User.query.get(payload['sub'])
        if user:
            return user
        return None
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

def generate_refresh_token(user_id):
    try:
        payload = {'exp': datetime.utcnow() + timedelta(days=7), 'iat': datetime.utcnow(), 'sub': user_id}
        refresh_token = jwt.encode(payload, secret_key, algorithm='HS256')
        return refresh_token
    except Exception as e:
        current_app.logger.error(f'Failed to generate refresh token: {e}')
        return None

def verify_refresh_token(token):
    try:
        payload = jwt.decode(token, secret_key, algorithms=['HS256'])
        user = User.query.get(payload['sub'])
        if user:
            return user
        return None
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

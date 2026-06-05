python
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime, timedelta
import jwt
from src.utils.db import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    token = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Token(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    expiration_date = db.Column(db.DateTime)

@current_app.route('/revoke_token', methods=['POST'])
def revoke_token():
    data = request.json
    token = data.get('token')
    Token.query.filter_by(token=token).delete()
    db.session.commit()
    return jsonify({'message': 'Token revoked successfully'})

def generate_token(user):
    payload = {
        'exp': datetime.utcnow() + timedelta(days=30),
        'iat': datetime.utcnow(),
        'sub': user.id
    }
    token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
    user.token = token.decode('UTF-8')
    db.session.commit()
    return token.decode('UTF-8')

def verify_token(token):
    try:
        payload = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=['HS256'])
        user = User.query.filter_by(id=payload.get('sub')).first()
        if user and user.token == token:
            return user
        return None
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None

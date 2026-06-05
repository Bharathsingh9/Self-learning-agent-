# Importing necessary libraries
from flask import Flask, request, jsonify, session, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os

# Initialize Flask application
app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret-key')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///scientific_calculator.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize Flask-Login and Flask-SQLAlchemy
db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Create User model for storing user credentials
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create Calculation model for storing user-created equations and formulas
class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equation = db.Column(db.String(128), nullable=False)
    formula = db.Column(db.String(128), nullable=True)
    created_by = db.Column(db.String(64), db.ForeignKey('user.username'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

# Create CalculatorHistory model for storing user calculation history
class CalculatorHistory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    equation = db.Column(db.String(128), nullable=False)
    result = db.Column(db.String(128), nullable=False)
    created_by = db.Column(db.String(64), db.ForeignKey('user.username'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

# Initialize routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register_user_route():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    if not username or not password:
        return jsonify({'error': 'Missing username or password'}), 400
    user = User.query.filter_by(username=username).first()
    if user:
        return jsonify({'error': 'Username already exists'}), 400
    new_user = User(username=username)
    new_user.set_password(password)
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User created successfully'})

@app.route('/login', methods=['POST'])
def login_user_route():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        login_user(user)
        return jsonify({'message': 'User logged in successfully'})
    return jsonify({'error': 'Invalid credentials'}), 401

@app.route('/logout', methods=['POST'])
@login_required
def logout_user_route():
    logout_user()
    return jsonify({'message': 'User logged out successfully'})

@app.route('/calculate', methods=['POST'])
@login_required
def calculate():
    data = request.get_json()
    equation = data.get('equation')
    if not equation:
        return jsonify({'error': 'No equation provided'}), 400
    try:
        # Note: eval is dangerous in production, but keeping it as requested for now
        # with some basic safety or use a safer approach if possible.
        result = eval(equation, {"__builtins__": None}, {"math": math})
        new_calculation = CalculatorHistory(equation=equation, result=str(result), created_by=current_user.username)
        db.session.add(new_calculation)
        db.session.commit()
        return jsonify({'result': result, 'message': 'Calculation done successfully'})
    except Exception as e:
        return jsonify({'error': f'Calculation error: {str(e)}'}), 400

@app.route('/get_calculations', methods=['GET'])
@login_required
def get_calculations():
    calculations = CalculatorHistory.query.filter_by(created_by=current_user.username).all()
    results = []
    for calculation in calculations:
        results.append({'equation': calculation.equation, 'result': calculation.result, 'at': calculation.created_at})
    return jsonify(results)

# Initialize database
with app.app_context():
    db.create_all()
    
# Run the application
if __name__ == '__main__':
    app.run(debug=True, port=8002)
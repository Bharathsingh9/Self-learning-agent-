python
# routes/calculation_routes.py

from flask import Blueprint, request, jsonify
from flask_sqlalchemy import SQLAlchemy

# Initialize the Flask application and database
from app import app, db

calculation_routes = Blueprint('calculation_routes', __name__, template_folder='templates')

# Define the Calculation model
class Calculation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    expression = db.Column(db.String(200), nullable=False)
    result = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'expression': self.expression,
            'result': self.result,
            'created_at': self.created_at.isoformat()
        }

# API Endpoints
@calculation_routes.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    if 'expression' not in data:
        return jsonify({'error': 'Missing expression'}), 400

    try:
        result = eval(data['expression'])
        calculation = Calculation(user_id=1, expression=data['expression'], result=str(result))
        db.session.add(calculation)
        db.session.commit()
        return jsonify(calculation.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@calculation_routes.route('/results', methods=['GET'])
def get_results():
    user_id = request.args.get('user_id')
    if user_id:
        results = Calculation.query.filter_by(user_id=user_id).all()
    else:
        results = Calculation.query.all()

    return jsonify([result.to_dict() for result in results])

@calculation_routes.route('/result/<int:calculation_id>', methods=['GET'])
def get_result(calculation_id):
    result = Calculation.query.get(calculation_id)
    if result:
        return jsonify(result.to_dict())
    else:
        return jsonify({'error': 'Result not found'}), 404

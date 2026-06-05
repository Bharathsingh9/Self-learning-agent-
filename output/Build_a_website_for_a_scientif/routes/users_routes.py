python
# routes/users_routes.py

from flask import Blueprint, request, jsonify
from user_api import db
from models import User, Calculation

# Create a blueprint for user routes
users_routes = Blueprint('users_routes', __name__)

# Route to process user calculations
@users_routes.route('/calculate', methods=['POST'])
def process_calculations():
    data = request.json
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
    
    try:
        num1 = float(data['num1'])
        num2 = float(data['num2'])
        operation = data['operation']
    except (KeyError, ValueError):
        return jsonify({'error': 'Invalid request'}), 400

    if operation not in ['+', '-', '*', '/']:
        return jsonify({'error': 'Invalid operation'}), 400

    result = None
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            return jsonify({'error': 'Cannot divide by zero'}), 400

    # Create a new calculation
    calculation = Calculation(num1=num1, num2=num2, operation=operation, result=result, user_id=data['user_id'])

    # Save the calculation in the database
    db.session.add(calculation)
    db.session.commit()

    # Return the result
    return jsonify({'result': result}), 200

# Route to get user calculations
@users_routes.route('/calculations', methods=['GET'])
def get_calculations():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    # Get the user's calculations from the database
    calculations = Calculation.query.filter_by(user_id=user_id).all()

    # Return the calculations as a list of dictionaries
    return jsonify([{
        'num1': calculation.num1,
        'num2': calculation.num2,
        'operation': calculation.operation,
        'result': calculation.result
    } for calculation in calculations])

# Route to get average calculation result
@users_routes.route('/average', methods=['GET'])
def get_average():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'User ID is required'}), 400

    # Get the user's calculations from the database
    calculations = Calculation.query.filter_by(user_id=user_id).all()

    # Calculate the average result
    if calculations:
        results = [calculation.result for calculation in calculations]
        average = sum(results) / len(results)
        return jsonify({'average': average})
    else:
        return jsonify({'average': 0})


This code assumes that you have the following:

* `flask` as an installed library for creating the API.
* `user_api` and `db` objects which are used to interact with the Flask app and database.
* `models` module with the `User` and `Calculation` classes.
* A database setup to store user calculations.
* The `request` object is used to handle HTTP requests and JSON data.
* The `jsonify` function is used to return JSON responses with error messages.
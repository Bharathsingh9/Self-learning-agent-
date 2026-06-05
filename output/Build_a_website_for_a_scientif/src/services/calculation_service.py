python
from typing import List
import json
import uuid

class CalculationService:
    def __init__(self):
        self.calculation_history = []
        self.id_counter = 0

    def perform_calculation(self, expression: str) -> dict:
        try:
            result = eval(expression)
            return {'success': True, 'result': result}
        except Exception as e:
            return {'success': False, 'error': str(e)}

    def get_calculation_history(self):
        return self.calculation_history

    def store_calculation(self, result):
        self.id_counter += 1
        self.calculation_history.append({
            'id': self.id_counter,
            'input': '',
            'result': result
        })

    def handle_user_input(self, input_str):
        input_json = json.loads(input_str)
        expression = input_json.get('expression')
        if expression:
            result = self.perform_calculation(expression)
            self.store_calculation(result)
            return result

def create_service():
    service = CalculationService()
    service.id_counter = 1  # reset id counter on each restart
    return service

class JsonCalculatorService:
    def __init__(self, service: CalculationService):
        self.service = service
        self.user_input_history = []
        self.id_counter = 0

    def handle_user_input(self, input_str):
        input_json = json.loads(input_str)
        expression = input_json.get('expression')
        if expression:
            result = self.service.perform_calculation(expression)
            self.service.store_calculation(result)
            user_input = {
                'id': self.id_counter + 1,
                'input': expression,
                'result': result
            }
            self.id_counter += 1
            self.user_input_history.append(user_input)
            return result
        return {"error": "Invalid input"}

def get_json_calculation_service():
    service = create_service()
    json_service = JsonCalculatorService(service)
    return json_service



# Using Flask for a simple HTTP Server
from flask import Flask, request, jsonify
from src.services.calculation_service import get_json_calculation_service

app = Flask(__name__)

json_service = get_json_calculation_service()

@app.route('/perform_calculation', methods=['POST'])
def perform_calculation():
    input_str = request.get_json().get('input')
    result = json_service.handle_user_input(input_str)
    return jsonify(result)

@app.route('/get_calculation_history', methods=['GET'])
def get_calculation_history():
    result = json_service.get_calculation_history()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)

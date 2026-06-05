python
# tests/test_calculation.py

import unittest
from your_app.app import app, db, Calculation
from your_app.config import TestingConfig
from your_app.main.forms import Form
from your_app.main.routes import index

class TestCalculation(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config.from_object(TestingConfig)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_calculate_sum(self):
        data = {'num1': 10, 'num2': 20, 'operator': '+'}
        response = self.app.post('/calculate', data=Form(data).data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Sum: 30', response.data.decode('utf-8'))

    def test_calculate_subtract(self):
        data = {'num1': 20, 'num2': 10, 'operator': '-'}
        response = self.app.post('/calculate', data=Form(data).data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Subtract: 10', response.data.decode('utf-8'))

    def test_calculate_multiply(self):
        data = {'num1': 10, 'num2': 20, 'operator': '*'}
        response = self.app.post('/calculate', data=Form(data).data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Multiply: 200', response.data.decode('utf-8'))

    def test_calculate_divide(self):
        data = {'num1': 20, 'num2': 5, 'operator': '/'}
        response = self.app.post('/calculate', data=Form(data).data, follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Divide: 4.0', response.data.decode('utf-8'))

class TestCalculationModel(unittest.TestCase):
    def test_add_calculation(self):
        calculation = Calculation(num1=10, num2=20, operator='+')
        db.session.add(calculation)
        db.session.commit()
        self.assertEqual(Calculation.query.count(), 1)

    def test_get_calculation(self):
        calculation = Calculation(num1=10, num2=20, operator='+')
        db.session.add(calculation)
        db.session.commit()
        self.assertEqual(Calculation.query.first().num1, 10)

    def test_delete_calculation(self):
        calculation = Calculation(num1=10, num2=20, operator='+')
        db.session.add(calculation)
        db.session.commit()
        self.assertEqual(Calculation.query.count(), 1)
        calculation_id = calculation.id
        db.session.delete(calculation)
        db.session.commit()
        self.assertEqual(Calculation.query.count(), 0)
        self.assertEqual(Calculation.query.filter_by(id=calculation_id).count(), 0)

if __name__ == '__main__':
    unittest.main()


Note: You will need to replace `your_app` with the actual name of your application. Also, make sure you have the necessary dependencies installed, such as Flask and Flask-SQLAlchemy.
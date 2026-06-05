python
# tests/test_user.py

import unittest
from yourproject.app import create_app, db
from yourproject.models import User, CalculatorSession

class TestUser(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app.config['TESTING'] = True
        self.app.config['WTF_CSRF_ENABLED'] = False
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + 'test.db'
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    # Testing User registration
    def test_user_registration(self):
        new_user = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password'
        }
        response = self.client.post('/register', data=new_user)
        self.assertEqual(response.status_code, 302)

    # Testing User login
    def test_user_login(self):
        new_user = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password'
        }
        self.client.post('/register', data=new_user)
        login_data = {
            'username': 'testuser',
            'password': 'password'
        }
        response = self.client.post('/login', data=login_data)
        self.assertEqual(response.status_code, 302)

    # Testing User logout
    def test_user_logout(self):
        new_user = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password'
        }
        self.client.post('/register', data=new_user)
        self.client.post('/login', data=new_user)
        response = self.client.get('/logout')
        self.assertEqual(response.status_code, 302)

    # Testing User access to calculator features
    def test_user_access_calculator(self):
        new_user = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password'
        }
        self.client.post('/register', data=new_user)
        self.client.post('/login', data=new_user)
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    # Testing User access to calculator features without login
    def test_user_denied_calculator_access(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 302)

    # Testing User access to calculator sessions
    def test_user_calculator_sessions(self):
        new_user = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password'
        }
        self.client.post('/register', data=new_user)
        self.client.post('/login', data=new_user)
        new_session = CalculatorSession(user_id=1, expression='1+1=2')
        with self.app.app_context():
            db.session.add(new_session)
            db.session.commit()
        response = self.client.get('/sessions')
        self.assertEqual(response.status_code, 200)

    # Testing User access to calculator session details
    def test_user_calculator_session_details(self):
        new_user = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password': 'password'
        }
        self.client.post('/register', data=new_user)
        self.client.post('/login', data=new_user)
        new_session = CalculatorSession(user_id=1, expression='1+1=2')
        with self.app.app_context():
            db.session.add(new_session)
            db.session.commit()
        response = self.client.get('/sessions/{}'.format(new_session.id))
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()

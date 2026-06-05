python
import unittest
from app import create_app
from app.models import User
from app import db

class AuthTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_register_user(self):
        user = User.register('new_user', 'password', 'new_user@example.com')
        self.assertEqual(user.username, 'new_user')
        self.assertEqual(user.email, 'new_user@example.com')

    def test_login_user(self):
        user = User.register('login_user', 'password', 'login_user@example.com')
        self.assertTrue(user is not None)

    def test_invalid_login(self):
        user = User.query.filter(User.username == 'invalid_user').first()
        self.assertFalse(user is not None)

    def test_password_verification(self):
        user = User.register('verify_user', 'password', 'verify_user@example.com')
        self.assertTrue(user.verify_password('password'))
        self.assertFalse(user.verify_password('wrong_password'))

    def test_change_password(self):
        user = User.register('change_user', 'password', 'change_user@example.com')
        user.set_password('new_password')
        self.assertTrue(user.verify_password('new_password'))

    def test_register_duplicate_user(self):
        User.register('duplicate_user', 'password', 'duplicate_user@example.com')
        user = User.query.filter(User.username == 'duplicate_user').first()
        self.assertFalse(user is None)
        with self.assertRaises(ValueError):
            User.register('duplicate_user', 'password', 'duplicate_user@example.com')

class AuthenticationTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()

    def test_register(self):
        response = self.client.post('/register', json={'username': 'new_user', 'password': 'password', 'email': 'new_user@example.com'})
        self.assertEqual(response.status_code, 201)

    def test_login(self):
        self.client.post('/register', json={'username': 'login_user', 'password': 'password', 'email': 'login_user@example.com'})
        response = self.client.post('/login', json={'username': 'login_user', 'password': 'password'})
        self.assertEqual(response.status_code, 200)

    def test_invalid_login(self):
        self.client.post('/register', json={'username': 'invalid_user', 'password': 'password', 'email': 'invalid_user@example.com'})
        response = self.client.post('/login', json={'username': 'invalid_user', 'password': 'password'})
        self.assertEqual(response.status_code, 401)

    def test_logout(self):
        self.client.post('/register', json={'username': 'logout_user', 'password': 'password', 'email': 'logout_user@example.com'})
        response = self.client.post('/login', json={'username': 'logout_user', 'password': 'password'})
        headers = {'Authorization': 'Bearer ' + response.json['token']}
        response = self.client.get('/logout', headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_unauthorized(self):
        self.client.get('/calculator', follow_redirects=True)
        self.assertEqual(self.client.status_code, 401)

    def test_admin_access(self):
        self.client.post('/register', json={'username': 'admin_user', 'password': 'password', 'email': 'admin_user@example.com', 'admin': True})
        self.client.post('/login', json={'username': 'admin_user', 'password': 'password'})
        headers = {'Authorization': 'Bearer ' + self.client.last_response.json['token']}
        self.client.get('/calculator', headers=headers)
        self.assertEqual(self.client.status_code, 200)

if __name__ == '__main__':
    unittest.main()

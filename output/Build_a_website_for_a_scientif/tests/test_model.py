python
import os
import unittest
from dotenv import load_dotenv
from models import db, Server
from app import create_app

load_dotenv()

class TestServerModel(unittest.TestCase):

    def setUp(self):
        self.app = create_app('testing')
        self.app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('TEST_DATABASE_URI')
        self.client = self.app.test_client()
        db.init_app(self.app)
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add(self):
        with self.app.app_context():
            server = Server(math='2+2', result='4', date='2024-01-01')
            db.session.add(server)
            db.session.commit()
            self.assertEqual(db.session.query(Server).count(), 1)

    def test_subtract(self):
        with self.app.app_context():
            server = Server(math='5-3', result='2', date='2024-01-02')
            db.session.add(server)
            db.session.commit()
            self.assertEqual(db.session.query(Server).count(), 2)

    def test_multiply(self):
        with self.app.app_context():
            server = Server(math='4*5', result='20', date='2024-01-03')
            db.session.add(server)
            db.session.commit()
            self.assertEqual(db.session.query(Server).count(), 3)

    def test_divide(self):
        with self.app.app_context():
            server = Server(math='8/2', result='4', date='2024-01-04')
            db.session.add(server)
            db.session.commit()
            self.assertEqual(db.session.query(Server).count(), 4)

    def test_invalid_operation(self):
        with self.app.app_context():
            server = Server(math='a+b', result=None, date='2024-01-05')
            db.session.add(server)
            db.session.commit()
            self.assertEqual(db.session.query(Server).count(), 5)
            self.assertIsNone(db.session.query(Server).first().result)

if __name__ == '__main__':
    unittest.main()

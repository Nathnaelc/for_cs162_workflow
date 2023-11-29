import unittest
from app import app, db
from models import User


class FlaskTestCase(unittest.TestCase):

    # Setup and teardown for the test suite
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        with app.app_context():
            db.create_all()

    def tearDown(self):
        with app.app_context():
            db.session.remove()
            db.drop_all()

    # Helper methods
    def register(self, email, password):
        return self.app.post('/register', data=dict(email=email, password=password), follow_redirects=True)

    def login(self, email, password):
        return self.app.post('/login', data=dict(email=email, password=password), follow_redirects=True)

    def logout(self):
        return self.app.get('/logout', follow_redirects=True)

    def submit_expression(self, expression):
        return self.app.post('/evaluate', data=dict(expression=expression), follow_redirects=True)

    # Test cases
    def test_user_registration(self):
        response = self.register('test@example.com', 'testpassword')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Account created successfully', response.data)

    def test_login(self):
        self.register('test@example.com', 'testpassword')
        response = self.login('test@example.com', 'testpassword')
        self.assertEqual(response.status_code, 200)
        # Instead of checking for a specific success message, check if the response
        # redirects to the dashboard, which indicates a successful login.
        self.assertTrue('/dashboard' in response.headers['Location'])

    def test_logout(self):
        self.register('test@example.com', 'testpassword')
        self.login('test@example.com', 'testpassword')
        response = self.logout()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Logged out successfully', response.data)

    def test_expression_evaluation(self):
        self.register('test@example.com', 'testpassword')
        self.login('test@example.com', 'testpassword')
        response = self.submit_expression('2 + 2')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Expression evaluated', response.data)
        # Assuming the result is displayed in the response
        self.assertIn(b'4', response.data)

    def test_user_history(self):
        self.register('test@example.com', 'testpassword')
        self.login('test@example.com', 'testpassword')
        self.submit_expression('3 + 3')
        response = self.app.get('/history', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'3 + 3', response.data)


if __name__ == '__main__':
    unittest.main()

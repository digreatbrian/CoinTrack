import unittest
from app import create_app, db
from app.models import User, Income, Expense, Category
from datetime import datetime

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        self.client = self.app.test_client()

        # Create a clean database
        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()
        self.app_context.pop()

    def test_add_income(self):
        with self.client:
            # Test your income addition logic
            pass

    def test_add_expense(self):
        with self.client:
            # Test your expense addition logic
            pass

if __name__ == '__main__':
    unittest.main()

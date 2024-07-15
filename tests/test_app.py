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
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_add_income(self):
        with self.client:
            category = Category(name='Salary')
            db.session.add(category)
            db.session.commit()

            response = self.client.post('/income/add', data={
                'amount': 1000,
                'source': 'Job',
                'category': category.id
            }, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Income added successfully!', response.data)

    def test_add_expense(self):
        with self.client:
            category = Category(name='Food')
            db.session.add(category)
            db.session.commit()

            response = self.client.post('/expenses/add', data={
                'amount': 50,
                'description': 'Groceries',
                'category': category.id
            }, follow_redirects=True)

            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Expense added successfully!', response.data)

if __name__ == '__main__':
    unittest.main()

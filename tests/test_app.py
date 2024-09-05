import unittest
from app import create_app, db
from app.models import User, FinanceEntry


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app.config['TESTING'] = True
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
        self.client = self.app.test_client()

        with self.app.app_context():
            db.create_all()

    def tearDown(self):
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_add_income(self):
        with self.app.app_context():
            # Create a user
            user = User(username='testuser', email='test@example.com', password='password')
            db.session.add(user)
            db.session.commit()

            # Add an income entry
            response = self.client.post('/income/add', data={
                'amount': 1000,
                'category': 'Salary',
                'description': 'Monthly Salary'
            })
            self.assertEqual(response.status_code, 200)

            # Verify the entry in the database
            income_entry = FinanceEntry.query.filter_by(description='Monthly Salary').first()
            self.assertIsNotNone(income_entry)
            self.assertEqual(income_entry.amount, 1000)

    def test_add_expense(self):
        with self.app.app_context():
            # Create a user
            user = User(username='testuser', email='test@example.com', password='password')
            db.session.add(user)
            db.session.commit()

            # Add an expense entry
            response = self.client.post('/expenses/add', data={
                'amount': 100,
                'category': 'Food',
                'description': 'Grocery Shopping'
            })
            self.assertEqual(response.status_code, 200)

            # Verify the entry in the database
            expense_entry = FinanceEntry.query.filter_by(description='Grocery Shopping').first()
            self.assertIsNotNone(expense_entry)
            self.assertEqual(expense_entry.amount, 100)


if __name__ == '__main__':
    unittest.main()

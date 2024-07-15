import unittest
from app import create_app, db
from app.models import Income, Expense, Category

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
        with self.app.app_context():
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

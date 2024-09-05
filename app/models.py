from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(150), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'


class FinanceEntry(db.Model):
    __tablename__ = 'finance_entries'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type = db.Column(db.String(50))
    category = db.Column(db.String(50))
    __mapper_args__ = {
        'polymorphic_identity': 'finance_entry',
        'polymorphic_on': type
    }

    def __repr__(self):
        return f'<FinanceEntry {self.amount} {self.description}>'

class Income(FinanceEntry):
    __tablename__ = 'incomes'
    id = db.Column(db.Integer, db.ForeignKey('finance_entries.id'), primary_key=True)
    source = db.Column(db.Integer, db.ForeignKey('finance_entries.category'))

    __mapper_args__ = {
        'polymorphic_identity': 'income',
        'inherit_condition': (id == FinanceEntry.id)
    }

    def __repr__(self):
        return f'<Income {self.amount} {self.description}>'

class Expense(FinanceEntry):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, db.ForeignKey('finance_entries.id'), primary_key=True)

    __mapper_args__ = {
        'polymorphic_identity': 'expense',
    }

    def __repr__(self):
        return f'<Expense {self.amount} {self.description}>'

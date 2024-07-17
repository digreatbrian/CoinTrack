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

    categories = db.relationship('Category', backref='user', lazy=True)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User {self.username}>'

class Category(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    entries = db.relationship('Entry', backref='category', lazy=True)

    def __repr__(self):
        return f'<Category {self.name}>'

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Float, nullable=False)
    description = db.Column(db.String(255))
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'entry',
        'polymorphic_on': type
    }

    def __repr__(self):
        return f'<Entry {self.amount} {self.description}>'

class Income(Entry):
    __tablename__ = 'incomes'
    id = db.Column(db.Integer, db.ForeignKey('entries.id'), primary_key=True)
    source = db.Column(db.String(100), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'income',
    }

class Expense(Entry):
    __tablename__ = 'expenses'
    id = db.Column(db.Integer, db.ForeignKey('entries.id'), primary_key=True)
    description = db.Column(db.String(255))

    __mapper_args__ = {
        'polymorphic_identity': 'expense',
    }

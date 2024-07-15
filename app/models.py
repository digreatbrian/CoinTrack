from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

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
    user = db.relationship('User', backref=db.backref('categories', lazy=True))

class Entry(db.Model):
    __tablename__ = 'entries'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)
    type = db.Column(db.String(50))

    __mapper_args__ = {
        'polymorphic_identity': 'entry',
        'polymorphic_on': type
    }

    user = db.relationship('User', backref=db.backref('entries', lazy=True))
    category = db.relationship('Category', backref=db.backref('entries', lazy=True))

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

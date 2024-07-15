from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FloatField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError
from .models import User, Category

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username is already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email is already in use.')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class IncomeForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    source = StringField('Source', validators=[DataRequired()])
    category = SelectField('Category', coerce=int)
    submit = SubmitField('Add Income')

    def __init__(self, *args, **kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id, category.name) for category in Category.query.all()]

class ExpenseForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    category = SelectField('Category', coerce=int)
    submit = SubmitField('Add Expense')

    def __init__(self, *args, **kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)
        self.category.choices = [(category.id, category.name) for category in Category.query.all()]

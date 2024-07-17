from flask import Blueprint

income = Blueprint('income', __name__)

@income.route('/income')
def show_income():
    return "Income Page"

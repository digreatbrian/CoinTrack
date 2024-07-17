from flask import Blueprint

expenses = Blueprint('expenses', __name__)

@expenses.route('/expenses')
def show_expenses():
    return "Expenses Page"

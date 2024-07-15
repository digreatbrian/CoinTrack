from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from .forms import RegistrationForm, LoginForm, IncomeForm, ExpenseForm
from .models import User, Income, Expense, Category, db

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Registration successful. You can now log in.')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid email or password.')
    return render_template('login.html', form=form)

@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))

@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/income/add', methods=['GET', 'POST'])
@login_required
def add_income():
    form = IncomeForm()
    if form.validate_on_submit():
        amount = form.amount.data
        source = form.source.data
        category_id = form.category.data

        new_income = Income(amount=amount, source=source, category_id=category_id)
        db.session.add(new_income)
        db.session.commit()
        flash('Income added successfully!', 'success')
        return redirect(url_for('main.income_list'))
    return render_template('add_income.html', form=form)

@main.route('/income/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_income(id):
    income = Income.query.get_or_404(id)
    form = IncomeForm()
    if form.validate_on_submit():
        income.amount = form.amount.data
        income.source = form.source.data
        income.category_id = form.category.data

        db.session.commit()
        flash('Income updated successfully!', 'success')
        return redirect(url_for('main.income_list'))
    elif request.method == 'GET':
        form.amount.data = income.amount
        form.source.data = income.source
        form.category.data = income.category_id
    return render_template('edit_income.html', form=form)

@main.route('/income/<int:id>/delete', methods=['POST'])
@login_required
def delete_income(id):
    income = Income.query.get_or_404(id)
    db.session.delete(income)
    db.session.commit()
    flash('Income deleted successfully!', 'success')
    return redirect(url_for('main.income_list'))

@main.route('/expenses/add', methods=['GET', 'POST'])
@login_required
def add_expense():
    form = ExpenseForm()
    if form.validate_on_submit():
        amount = form.amount.data
        description = form.description.data
        category_id = form.category.data

        new_expense = Expense(amount=amount, description=description, category_id=category_id)
        db.session.add(new_expense)
        db.session.commit()
        flash('Expense added successfully!', 'success')
        return redirect(url_for('main.expense_list'))
    return render_template('add_expense.html', form=form)

@main.route('/expenses/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_expense(id):
    expense = Expense.query.get_or_404(id)
    form = ExpenseForm()
    if form.validate_on_submit():
        expense.amount = form.amount.data
        expense.description = form.description.data
        expense.category_id = form.category.data

        db.session.commit()
        flash('Expense updated successfully!', 'success')
        return redirect(url_for('main.expense_list'))
    elif request.method == 'GET':
        form.amount.data = expense.amount
        form.description.data = expense.description
        form.category.data = expense.category_id
    return render_template('edit_expense.html', form=form)

@main.route('/expenses/<int:id>/delete', methods=['POST'])
@login_required
def delete_expense(id):
    expense = Expense.query.get_or_404(id)
    db.session.delete(expense)
    db.session.commit()
    flash('Expense deleted successfully!', 'success')
    return redirect(url_for('main.expense_list'))

@main.route('/income', methods=['GET'])
@login_required
def income_list():
    incomes = Income.query.all()
    return render_template('income_list.html', incomes=incomes)

@main.route('/expenses', methods=['GET'])
@login_required
def expense_list():
    expenses = Expense.query.all()
    return render_template('expense_list.html', expenses=expenses)

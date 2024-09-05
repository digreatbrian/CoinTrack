from flask import render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Expense, db
from app.forms import ExpenseForm
from app.routes import main


@main.route('/expenses', methods=['GET'])
@login_required
def expense_list():
	expenses = Expense.query.all()
	return render_template('expense_list.html', expenses=expenses)


@main.route('/expenses/add', methods=['GET', 'POST'])
@login_required
def add_expense():
	form = ExpenseForm()
	if form.validate_on_submit():
		amount = form.amount.data
		description = form.description.data

		new_expense = Expense(amount=amount, description=description, user_id=current_user.id, category=form.category.data)
		db.session.add(new_expense)
		db.session.commit()
		flash('Expense added successfully!', 'success')
		return redirect(url_for('main.expense_list'))
	else:
		if request.method == 'POST':
			flash('Please make sure that all fields are provided with correct input!', 'error')
	return render_template('add_expense.html', form=form)


@main.route('/expenses/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_expense(id):
	expense = Expense.query.get_or_404(id)
	form = ExpenseForm()
	if form.validate_on_submit():
		expense.amount = form.amount.data
		expense.description = form.description.data
		expense.category = form.category.data

		db.session.commit()
		flash('Expense updated successfully!', 'success')
		return redirect(url_for('main.expense_list'))
	else:
		if request.method == 'POST':
			flash('Please make sure that all fields are provided with correct input!', 'error')
	if request.method == 'GET':
		form.amount.data = expense.amount
		form.description.data = expense.description
		form.category.data = expense.category
	return render_template('edit_expense.html', form=form)


@main.route('/expenses/<int:id>/delete', methods=['POST'])
@login_required
def delete_expense(id):
	expense = Expense.query.get_or_404(id)
	db.session.delete(expense)
	db.session.commit()
	flash('Expense deleted successfully!', 'success')
	return redirect(url_for('main.expense_list'))

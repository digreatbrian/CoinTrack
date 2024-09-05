from flask import render_template, redirect, url_for, flash, request
from app.models import Income, db
from flask_login import login_required, current_user
from app.forms import IncomeForm
from app.routes import main


@main.route('/income', methods=['GET'])
@login_required
def income_list():
	incomes = Income.query.all()
	return render_template('income_list.html', incomes=incomes)


@main.route('/income/add', methods=['GET', 'POST'])
@login_required
def add_income():
	form = IncomeForm()

	if form.validate_on_submit():
		amount = form.amount.data
		source = form.source.data
		user_id = current_user.id
		description = form.description.data

		new_income = Income(amount=amount, source=source, user_id=user_id, description=description)
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
		income.description = form.description.data

		db.session.commit()
		flash('Income updated successfully!', 'success')
		return redirect(url_for('main.income_list'))
	else:
		if request.method == 'POST':
			flash('Please make sure that all fields are provided with correct input!', 'error')
	if request.method == 'GET':
		form.amount.data = income.amount
		form.source.data = income.source
		form.description.data = income.description

	return render_template('edit_income.html', form=form)


@main.route('/income/<int:id>/delete', methods=['POST'])
@login_required
def delete_income(id):
	income = Income.query.get_or_404(id)
	db.session.delete(income)
	db.session.commit()
	flash('Income deleted successfully!', 'success')
	return redirect(url_for('main.income_list'))

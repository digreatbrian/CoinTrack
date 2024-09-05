from flask import render_template
from flask_login import login_required, current_user
from sqlalchemy import func, text
from app.models import Income, Expense, db
from app.routes import main
from app.utils import human_readable_format, human_readable_money_format, human_readable_percentage_format


@main.route('/dashboard')
@login_required
def dashboard():
	"""
    Dashboard view function that displays the user's financial dashboard.
    Requires the user to be logged in.
    """

	user = current_user

	def get_user_income() -> int | float:
		"""
        Get the total income of the current user.

        Returns:
            int | float: Total income amount.
        """
		return db.session.query(func.sum(Income.amount)).filter_by(user_id=user.id).scalar() or 0

	def get_user_expenses() -> int | float:
		"""
        Get the total expenses of the current user.

        Returns:
            int | float: Total expenses amount.
        """
		return db.session.query(func.sum(Expense.amount)).filter_by(user_id=user.id).scalar() or 0

	def get_user_net_worth() -> int | float:
		"""
        Calculate the net worth of the current user.

        Returns:
            int | float: Net worth amount.
        """
		print('Calculating net worth...', get_user_income(), get_user_expenses())
		return get_user_income() - get_user_expenses()

	def get_debt_to_income_ratio() -> int | float:
		"""
        Calculate the debt-to-income ratio of the current user.

        Returns:
            int | float: Debt-to-income ratio.
        """
		if get_user_income() == 0:
			return 0
		return (get_user_expenses() / get_user_income()) * 100

	def get_savings_rate() -> int | float:
		"""
        Calculate the savings rate of the current user.

        Returns:
            int | float: Savings rate.
        """
		if get_user_income() == 0:
			return 0
		return ((get_user_income() - get_user_expenses()) / get_user_income()) * 100

	def get_dominant_expense_category() -> str:
		"""
        Get the dominant expense category of the current user.

        Returns:
            str: Dominant expense category.
        """
		result = db.session.query(Expense.category, func.count(Expense.category).label('category_count')) \
			.filter_by(user_id=user.id) \
			.group_by(Expense.category) \
			.order_by(text('category_count DESC')) \
			.first()
		return result.category if result else None

	def get_dominant_expense_category_amount(category: str) -> int | float:
		"""
        Get the total amount spent in the dominant expense category.

        Args:
            category (str): Expense category.

        Returns:
            int | float: Total amount spent in the category.
        """
		return db.session.query(func.sum(Expense.amount)).filter_by(user_id=user.id, category=category).scalar() or 0

	def get_dominant_expense_category_percentage() -> int | float:
		"""
        Calculate the percentage of the dominant expense category.

        Returns:
            int | float: Percentage of the dominant expense category.
        """
		dominant_category_count = Expense.query.filter_by(user_id=user.id).filter_by(
			category=get_dominant_expense_category()).count()
		if dominant_category_count == 0:
			return 0
		return (dominant_category_count / Expense.query.filter_by(user_id=user.id).count()) * 100

	def get_dominant_income_source() -> str:
		"""
        Get the dominant income source of the current user.

        Returns:
            str: Dominant income source.
        """
		result = db.session.query(Income.source, func.count(Income.source).label('source_count')) \
			.filter_by(user_id=user.id) \
			.group_by(Income.source) \
			.order_by(text('source_count DESC')) \
			.first()
		return result.source if result else None

	def get_dominant_income_source_amount(source: str) -> int | float:
		"""
        Get the total amount earned from the dominant income source.

        Args:
            source (str): Income source.

        Returns:
            int | float: Total amount earned from the source.
        """
		return db.session.query(func.sum(Income.amount)).filter_by(user_id=user.id, source=source).scalar() or 0

	def get_dominant_income_source_percentage() -> int | float:
		"""
        Calculate the percentage of the dominant income source.

        Returns:
            int | float: Percentage of the dominant income source.
        """
		dominant_income_source_count = Income.query.filter_by(user_id=user.id).filter_by(
			source=get_dominant_income_source()).count()
		if dominant_income_source_count == 0:
			return 0
		return (dominant_income_source_count / Income.query.filter_by(user_id=user.id).count()) * 100

	def get_financial_progress() -> int | float:
		"""
        Calculate the financial progress of the current user.

        Returns:
            int | float: Financial progress.
        """
		net_worth = get_user_net_worth()
		if net_worth <= 0:
			return 0
		return net_worth / get_user_income()

	def get_financial_progress_percentage() -> int | float:
		"""
        Calculate the financial progress percentage of the current user.

        Returns:
            int | float: Financial progress percentage.
        """
		net_worth = get_user_net_worth()
		if net_worth <= 0:
			return 0
		return (net_worth / get_user_income()) * 100

	def get_value_or_error(_func):
		"""
        Execute a function and handle any errors.

        Args:
            _func (function): Function to execute.

        Returns:
            Any: Result of the function or the error.
        """
		try:
			return _func()
		except Exception as e:
			print(f'Error: {e}')
			raise
			return e

	def build_context() -> dict:
		"""
        Build the context dictionary for the dashboard template.

        Returns:
            dict: Context dictionary with financial data.
        """
		context = {
			'income': human_readable_money_format(get_value_or_error(get_user_income)),
			'expenses': human_readable_money_format(get_value_or_error(get_user_expenses)),
			'net_worth': human_readable_money_format(get_value_or_error(get_user_net_worth)),
			'debt_to_income_ratio': human_readable_percentage_format(get_value_or_error(get_debt_to_income_ratio)),
			'savings_rate': human_readable_percentage_format(get_value_or_error(get_savings_rate)),
			'dominant_expense': get_value_or_error(get_dominant_expense_category),
			'dominant_expense_percentage': human_readable_percentage_format(
				get_value_or_error(get_dominant_expense_category_percentage)),
			'dominant_income': get_value_or_error(get_dominant_income_source),
			'dominant_income_percentage': human_readable_percentage_format(
				get_value_or_error(get_dominant_income_source_percentage)),
			'financial_progress': human_readable_format(get_value_or_error(get_financial_progress)),
			'financial_progress_percentage': human_readable_percentage_format(
				get_value_or_error(get_financial_progress_percentage)),
		}
		dominant_income_source = context['dominant_income']
		dominant_expense_category = context['dominant_expense']

		if dominant_income_source:
			context['dominant_income_amount'] = human_readable_money_format(
				get_value_or_error(lambda: get_dominant_income_source_amount(dominant_income_source)))

		if dominant_expense_category:
			context['dominant_expense_amount'] = human_readable_money_format(
				get_value_or_error(lambda: get_dominant_expense_category_amount(dominant_expense_category)))

		return context

	def add_context_data_statuses(context):
		def convert_to_float(value):
			if isinstance(value, (int, float)):
				return value
			if isinstance(value, str):
				value = value.replace(' ', '').replace("$", "").replace(",", "").replace("%", "")
			try:
				return float(value)
			except ValueError:
				return value

		# networth status
		net_worth = convert_to_float(context.get('net_worth'))
		debt_to_income_ratio = convert_to_float(context.get('debt_to_income_ratio'))
		savings_rate = convert_to_float(context.get('savings_rate'))
		financial_progress_percentage = convert_to_float(context.get('financial_progress_percentage'))

		if isinstance(net_worth, float):
			# right now we are only checking net worth
			if net_worth < 0:
				context['net_worth_status'] = 'negative'
			elif net_worth > 0:
				context['net_worth_status'] = 'positive'
			else:
				context['net_worth_status'] = 'neutral'
		else:
			context['net_worth_status'] = 'error'

		if isinstance(debt_to_income_ratio, float):
			if debt_to_income_ratio > 43:
				context['debt_to_income_ratio_status'] = 'negative'
			elif debt_to_income_ratio == 0:
				context['debt_to_income_ratio_status'] = 'neutral'
			else:
				context['debt_to_income_ratio_status'] = 'positive'
		else:
			context['debt_to_income_ratio_status'] = 'error'

		if isinstance(savings_rate, float):
			if savings_rate < 20:
				context['savings_rate_status'] = 'negative'
			elif savings_rate > 20:
				context['savings_rate_status'] = 'positive'
			else:
				context['savings_rate_status'] = 'neutral'
		else:
			context['savings_rate_status'] = 'error'

		if isinstance(financial_progress_percentage, float):
			if financial_progress_percentage < 0:
				context['financial_progress_status'] = 'negative'
			elif financial_progress_percentage > 0:
				context['financial_progress_status'] = 'positive'
			else:
				context['financial_progress_status'] = 'neutral'
		else:
			context['financial_progress_status'] = 'error'

	context = build_context()
	add_context_data_statuses(context)

	return render_template('dashboard.html', **context)


def human_readable_format(value):
	"""
    Format the value to a human-readable format.
    - Floats are formatted to two decimal places.
    - Integers are formatted with spaces for thousands.

    Args:
        value (int | float): The value to be formatted.

    Returns:
        int | float | str: The formatted value.
    """
	if value is None:
		return value
	if isinstance(value, float):
		return float(f"{value:.2f}")
	if isinstance(value, int):
		return "{:,}".replace(",", " ")
	return value


def human_readable_money_format(value):
	"""
    Format the value to a human-readable money format.
    - Floats are formatted to two decimal places with a dollar sign and spaces for thousands.
    - Integers are formatted with a dollar sign and spaces for thousands.

    Args:
        value (int | float): The value to be formatted.

    Returns:
        int | float | str: The formatted value.
    """
	if value is None:
		return value
	if isinstance(value, float):
		return f"${value:,.2f}".replace(",", " ")
	if isinstance(value, int):
		return f"${value:,}".replace(",", " ")
	return value


def human_readable_percentage_format(value):
	"""
    Format the value to a human-readable percentage format.
    - Floats are formatted to two decimal places with a percentage sign.
    - Integers are formatted with spaces for thousands and a percentage sign.

    Args:
        value (int | float): The value to be formatted.

    Returns:
        int | float | str: The formatted value.
    """
	if value is None:
		return value
	if isinstance(value, float):
		return f"{value:.2f}%"
	if isinstance(value, int):
		return f"{value:,}".replace(",", " ") + "%"
	return value

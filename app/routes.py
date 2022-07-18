from config import config
from flask import render_template
from app import app
from app.adapters import categories_adapter, income_adapter, expenses_adapter
from app.api import get_categories, get_first_sheet_data
from app.utils import get_categories_balance_with_total


@app.route("/")
def index():
    categories = categories_adapter(get_categories())
    income = income_adapter(get_first_sheet_data(
        config['api_file_name'], config['document_name']))
    expenses = expenses_adapter(get_first_sheet_data(
        config['api_file_name'], config['document_name']))

    if sum([category['absoluteAmount'] for category in categories]) != 100:
        raise Exception('The sum of absoluteAmounts must be 100')

    categories_balance = get_categories_balance_with_total(
        categories, income, expenses)

    return render_template('index.html', categories_balance=categories_balance)


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")

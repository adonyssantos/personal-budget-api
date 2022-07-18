from config import config
from src.adapters import categories_adapter, income_adapter, expenses_adapter
from src.api import get_categories, get_first_sheet_data
from src.utils import get_categories_balance_with_total


def main():
    categories = categories_adapter(get_categories())
    income = income_adapter(get_first_sheet_data(
        config['api_file_name'], config['document_name']))
    expenses = expenses_adapter(get_first_sheet_data(
        config['api_file_name'], config['document_name']))

    if sum([category['absoluteAmount'] for category in categories]) != 100:
        raise Exception('The sum of absoluteAmounts must be 100')

    print(get_categories_balance_with_total(categories, income, expenses))

from src.data import categories, entradas, salidas
from src.utils import get_categories_balance_with_total


if __name__ == '__main__':
    if sum([category['absoluteAmount'] for category in categories]) != 100:
        raise Exception('The sum of absoluteAmounts must be 100')

    print(get_categories_balance_with_total(categories, entradas, salidas))

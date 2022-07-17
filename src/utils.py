def get_total_balance(income, expenses):
    balance = 0

    # Calculate the balance total income
    for entry in income:
        balance += entry['amount']

    # Subtract the balance total expenses
    for expense in expenses:
        balance -= expense['amount']

    return balance


def get_categories_balance(categories, income, expenses):
    categories_balance = []
    total_income = 0

    # Calculate the balance total income
    for entry in income:
        total_income += entry['amount']

    # Create a category balance for each category
    for category in categories:
        categories_balance.append({
            'name': category['name'],
            'balance': total_income * (category['absoluteAmount'] / 100)
        })

    # Update the balance of the category in the categories_balance list
    for expense in expenses:
        for category in categories_balance:
            if category['name'] == expense['category']:
                category['balance'] -= expense['amount']

    return categories_balance


def get_categories_balance_with_total(categories, income, expenses):
    categories_balance = get_categories_balance(categories, income, expenses)
    total_balance = get_total_balance(income, expenses)

    categories_balance.append({
        'name': 'Total',
        'balance': total_balance
    })

    return categories_balance

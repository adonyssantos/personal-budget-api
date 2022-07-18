def categories_adapter(data):
    adapted_data = []

    for category in data:
        adapted_data.append({
            'name': category['name'],
            'absoluteAmount': category['absoluteAmount'],
        })

    return adapted_data


def income_adapter(data):
    adapted_data = []

    for row in data:
        if row['Input Type'] == 'Incoming':
            adapted_data.append({
                'date': row['Income Date'],
                'amount': row['Income Amount'],
                'description': row['Income Description'],

            })

    return adapted_data


def expenses_adapter(data):
    adapted_data = []

    for row in data:
        if row['Input Type'] == 'Expensing':
            adapted_data.append({
                'date': row['Expense Date'],
                'amount': row['Amount Spent'],
                'description': row['Expense Description'],
                'category': row['Expense Category'],
            })

    return adapted_data

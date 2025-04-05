from datetime import datetime

def get_days_from_today(date):
    try:
        formatted_date = datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.today().date()
        return (formatted_date - current_date).days
    except ValueError:
        return "Incorrectly entered data. Enter in the format: 'YYYY-MM-DD'"

print(get_days_from_today('2025-12-31'))




import random

def get_numbers_ticket(min, max, quantity):

    if min < 1 or max > 1000 or quantity > (max - min + 1) or quantity < 1:
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)
    return sorted(numbers)

print(get_numbers_ticket(10,14,6))

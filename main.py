from datetime import datetime

def get_days_from_today(date):
    try:
        formated_date = datetime.strptime(date, '%Y-%m-%d').date()
        current_date = datetime.today().date()
        return (formated_date - current_date).days
    except ValueError:
        return "Incorrectly entered data. Enter in the format: 'YYYY-MM-DD'"

print(get_days_from_today('2025-12-31'))
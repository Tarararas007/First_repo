from datetime import datetime

def get_days_from_today(date):
    formated_date = datetime.strptime(date, '%Y-%m-%d').date()
    current_date = datetime.today().date()
    return (formated_date - current_date).days

print(get_days_from_today('2025-12-31'))
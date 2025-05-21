
def total_salary(path):
    total = 0
    count = 0
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                parts = line.strip().split(',')
                if parts[1].isdigit():
                    try:
                        salary = float(parts[1])
                        total += salary
                        count += 1
                    except ValueError:
                        continue
        average = total / count
        return f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}"
    except FileNotFoundError:
        return f"Файл за шляхом '{path}' не знайдено."

print(total_salary('salaries.txt'))
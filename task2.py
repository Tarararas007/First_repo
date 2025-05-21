
def get_cats_info(path):
    cats_info =[]
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line_number, lines in enumerate(file, start=1):
                parts = lines.strip().split(',')
                if len(parts) != 3:
                    print(f"Попередження: Неправильний формат у рядку {line_number}")
                    continue
                cat_id, name, age = parts
                try:
                    cat_dict = {
                        'id': cat_id,
                        'name': name,
                        'age': int(age)
                    }
                    cats_info.append(cat_dict)
                    print(cat_dict)
                except ValueError:
                    print(f"Попередження: Невірний вік у рядку {line_number}: {age}")
    except FileNotFoundError:
        print(f"Помилка: Файл за шляхом '{path}' не знайдено.")
    return cats_info

get_cats_info('cats.txt')
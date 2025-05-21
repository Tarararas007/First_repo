'''
Перше завдання
'''

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

'''
Друге завдання
'''

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

'''
Четверте завдання
'''

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    if len(args) != 2:
        return 'Error: Enter name and phone number.'
    name, phone = args
    name = name.lower()
    contacts[name] = phone
    return 'Contact added.'

def change_contact(args, contacts):
    if len(args) != 2:
        return 'Error: Enter name and new phone number.'
    name, phone = args
    name = name.lower()
    if name in contacts:
        contacts[name] = phone
        return 'Contact updated.'
    else:
        return 'Contact not found.'

def show_phone(args, contacts):
    if len(args) != 1:
        return 'Error: Enter one name to search.'
    name = args[0].lower()
    if name in contacts:
        return contacts[name]
    else:
        return 'Contact not found.'
    
def show_all(contacts):
    if not contacts:
        return 'No contacts found.'
    result = []
    for name, phone in contacts.items():
        result.append(f'{name}: {phone}')
    return '\n'.join(result)

def main():
    contacts = {}
    print("Welcome to assistant bot!")
    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print('Good bay!')
            break
        elif command == 'hello':
            print('How can i halp you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command == 'phone':
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print('Invalid command.')

if __name__ == "__main__":
    main()

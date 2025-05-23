
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

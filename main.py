# Команда "add [ім'я] [номер телефону]". Для цієї команди зробимо функцію add_contact:
# Введення: "add John 1234567890"
# Вивід: "Contact added."

# Команда "change [ім'я] [новий номер телефону]". Для цієї команди зробимо функцію change_contact:
# Введення: "change John 0987654321"
# Вивід: "Contact updated." або повідомлення про помилку, якщо ім'я не знайдено

# Команда "phone [ім'я]". Для цієї команди зробимо функцію show_phone:
# Введення: "phone John"
# Вивід: [номер телефону] або повідомлення про помилку, якщо ім'я не знайдено

# Команда "all". Для цієї команди зробимо функцію show_all:
# Введення: "all"
# Вивід: усі збережені контакти з номерами телефонів

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Sorry, {name} isn't exist."

def show_phone(args, contacts):
    name = args
    if name in contacts:
        phone = contacts[name]
        return "{name}: {phone}"
    else:
        return "Sorry, {name} isn't exist. Use 'add' for append this contact."
    
def show_all(contacts):
    res = []
    res.append("{:^20}".format("CONTACTS"))
    res.append("{:^20}".format("-"*10))
    for name, phone in contacts.items():
        res.append("{:<8} {} ".format(name+":", phone))
    res.append("{:^20}".format("="*20))
    return "\n".join(res)

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit", "good bye"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
            # print("{:^20}".format("CONTACTS"))
            # for name, phone in contacts.items():
            #     print("{:<8} {} ".format(name+":", phone))
            # print("{:>20} ".format("Done"))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()


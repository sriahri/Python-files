def display(names):
    for name in names:
        print(name)


def add(names, emails, numbers):
    name = input("Enter the name: ")
    email = input("Enter the email: ")
    number = input('Enter the number: ')
    names.append(name)
    emails.append(email)
    numbers.append(number)


def view(names, emails, numbers):
    name = input('Enter the name: ')
    if name in names:
        place = names.index(name)
        print('Name: {}, Email: {}, Number: {}'.format(names[place], emails[place], numbers[place]))


def delete(names, emails, numbers):
    name = input("Enter the name you want to delete: ")
    if name in names:
        place = names.index(name)
        names.pop(place)
        emails.pop(place)
        numbers.pop(place)
    else:
        print('Name not found')


def edit_phone(names, emails, numbers):
    name = input("Enter the name you want to edit the number: ")
    if name in names:
        place = names.index(name)
        number = input('Enter the number: ')
        numbers[place] = number
    else:
        print('Name not found')


def show_title():
    print("Contact Manager")
    print()


def show_menu():
    print("COMMAND MENU")


print("list - Show all contacts", end="\t")
print("view - View a contact")
print("edit - Edit phone number", end="\t")
print("add - Add a contact")
print("del - Delete a contact", end=" \t")
print("exit - Exit program")
print()


def main():
    contacts_names = ["Harry Potter", "Ron Weasley"]
    contacts_emails = ["hpotter@hogwarts.edu", "rweasley@hogwarts.edu"]
    contacts_numbers = ["+44 20 6789 0022", "+44 20 2345 0958"]

    show_title()
    show_menu()

    while True:
        command = input("Command: ")
        if command == "list":
            display(contacts_names)
        elif command == "view":
            view(contacts_names, contacts_emails, contacts_numbers)
        elif command == "add":
            add(contacts_names, contacts_emails, contacts_numbers)
        elif command == "del":
            delete(contacts_names, contacts_emails, contacts_numbers)
        elif command == "edit":
            edit_phone(contacts_names, contacts_emails, contacts_numbers)
        elif command == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")


if __name__ == "__main__":
    main()

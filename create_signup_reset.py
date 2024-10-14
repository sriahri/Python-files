import sys


def check_password(password):
    if password:
        upper_case_letters = sum(1 for i in password if i.isupper())
        numbers = sum(1 for i in password if i.isdigit())
        if len(password) > 7 and upper_case_letters > 1 and numbers > 1:
            for i in password:
                if i not in [' ', '=', '?', '\t']:
                    return True
        return False


def get_password():
    password = input("Enter the password: ")
    if check_password(password):
        second_password = input("Enter the password again to confirm: ")
        if second_password == password:
            return password
        else:
            get_password()


def write_to_file(file, data_dict):
    for username, password in data_dict.items():
        print(username, password)
        file.write('\n'+username+','+password)


while True:
    data_dict = {}
    file = open("password.txt", 'w+')
    lines = file.readlines()
    for i in lines:
        username, password = i.split(',')
        username = username.strip("\n")
        password = password.strip('\n')
        data_dict[username] = password
    print("The number of users are {}".format(len(data_dict.keys())))
    print("1. Sign up for the application")
    print("2. Change password")
    print("q. Quit")
    choice = input("Enter your choice: ")
    if choice.lower() == 'q':
        sys.exit(0)
    elif choice == '1':
        username = input("Enter the username: ")
        while username in data_dict.keys():
            print("Username already picked, please use other...")
        password = get_password()
        data_dict[username] = password
    elif choice == '2':
        username = input("Enter the username: ")
        if username not in data_dict.keys():
            print("Username does not exist")
        else:
            password = data_dict[username]
            user_password = input("Enter the old password: ")
            if user_password == password:
                password = get_password()
            data_dict[username] = password
    write_to_file(file, data_dict)
    file.close()


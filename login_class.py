class Login:
    def __init__(self, username=None, password=None):
        self.username = username
        self.password = password

    def check_details(self):
        if self.username.lower() == "jack" and self.password == "password":
            return True
        else:
            return False


if __name__ == '__main__':
    first_name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    uname = input("Enter the username: ")
    pwd = input("Enter the password: ")

    login = Login(uname, pwd)
    if login.check_details():
        print("Welcome {}, {} it is great to see you again!".format(first_name, last_name))
    else:
        print("Username or password incorrect. Try again!")

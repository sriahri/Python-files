def isPopular(name):
    name = name.lower()
    if name in ['mary', 'jennifer']:
        return True
    return False


if __name__ == '__main__':
    name = input("Enter your mother's name: ")
    if isPopular(name):
        print("That's a popular name!")
    else:
        print("That's an unusual name!")
details = {}


def menu():
    print('1. Search for a student')
    print('2. Add students details to the file')
    print('3. Retrieve students details')
    print('4. Exit')


def searchStudent():
    last_name = input("Enter the last name: ")
    if last_name in details:
        return details[last_name]


def addtoFile():
    f = open("studentDetails.txt", 'w')
    for i in details.keys():
        f.write(i)
        values = details[i]
        for value in values:
            f.write(', ')
            f.write(value)
        f.write("\n")
    print("Students details have been successfully saved!")


def getData():
    f = open("studentDetails.txt", 'r')
    lines = f.readlines()
    for line in lines:
        line = line.strip("\n").strip()
        last_name, first_name, level_of_education, age = line.split(', ')
        details[last_name] = [first_name, level_of_education, age]


def exit():
    print("Goodbye!")
    import sys
    sys.exit(0)


if __name__ == '__main__':
    number_of_students = int(input("Enter the number of students: "))
    for i in range(number_of_students):
        last_name = input("Enter the last name of the student: ")
        first_name = input("Enter the first name of the student: ")
        level_of_education = input("Enter the level of education of the student: ")
        age = input("Enter the age of the student: ")
        details[last_name] = [first_name, level_of_education, age]
    while True:
        menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            print(searchStudent())
        elif choice == 2:
            addtoFile()
        elif choice == 3:
            getData()
        elif choice == 4:
            exit()

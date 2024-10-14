names = ["Alice", "Bob", "Cindy"]
titles = ["CEO", "CFO", "VP"]
salaries = [482921, 628313, 124905]


# Adds an employee with the given name, title, and salary.
def addEmployee(name, title, salary):
    global names  # Gives function permission to use names list
    global titles
    global salaries
    names.append(name)  # Adds new name to names list
    titles.append(title)
    salaries.append(salary)


# Prints information on all employees.
def printEmployees():
    for i in range(len(names)):
        print(names[i] + "\t" + titles[i] + "\t${:.2f}".format(salaries[i]))


def printEmployee(name):
    for i in range(len(names)):
        if names[i].lower() == name.lower():
            print("Name: {} Title: {} Salary: {}".format(names[i], titles[i], salaries[i]))
            break
    else:
        print("Employee not found")


def calc_payroll():
    return sum(salaries)/12


def highest_paid():
    highest = salaries[0]
    place = 0
    for i in range(len(names)):
        if salaries[i] > highest:
            place = i
    print("The highest paid employee is {}".format(names[place]))


def raise_salary(name, percentage):
    for i in range(len(names)):
        if names[i].lower() == name.lower():
            salaries[i] += salaries[i] * (percentage*100)
            break
    else:
        print("Employee not found")


def fire_employee(name):
    for i in range(len(names)):
        if names[i].lower() == name.lower():
            names.pop(i)
            salaries.pop(i)
            titles.pop(i)
            break
    else:
        print("Employee not found")


def print_employee_with_title(job_title):
    for i in range(len(names)):
        if titles[i].lower() == job_title.lower():
            print("The employee name with {} title is {}".format(job_title, names[i]))
            break

    else:
        print("Employee not found")


# Main Test Program
def main():
    while True:
        print("1. Add Employee\n2. Fire employee\n3. print Employee\n4. print all Employees\n5. Give raise\n6. print "
              "monthly quarter roll\n7. Quit")
        choice = int(input("Enter the choice: "))
        if choice == 1:
            n = input("Enter new employee name: ")
            t = input("Enter " + n + "'s title: ")
            s = float(input("Enter " + n + "'s annual salary: $"))
            addEmployee(n, t, s)  # Test addEmployee function

        elif choice == 2:
            n = input("Enter new employee name: ")
            fire_employee(n)
        elif choice == 3:
            n = input("Enter new employee name: ")
            printEmployee(n)
        elif choice == 4:
            printEmployees()

        elif choice == 5:
            n = input("Enter new employee name: ")
            percentage = float(input("Enter precentage increase: "))
            raise_salary(n, percentage)

        elif choice == 6:
            print("The payroll is {}".format(calc_payroll()))

        else:
            break


if __name__ == '__main__':
    main()
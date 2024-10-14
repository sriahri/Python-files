class Employee:
    def __init__(self, name=None, age=None):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age

    def get_name(self):
        return self.name

    def displayName(self):
        print('The name of employee is {}'.format(self.name))

    def displayAge(self):
        print('The age of employee is {}'.format(self.age))


if __name__ == '__main__':
    employee = Employee('Jack', 21)
    print(employee.get_name())
    print(employee.get_age())
    employee = Employee('Steve', 32)
    employee.displayName()
    employee.displayAge()

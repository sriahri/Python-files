class Student:
    def __init__(self, name, age, address, uni, sn, empl):
        self.name = name
        self.age = age
        self.address = address
        self.uni = uni
        self.sn = sn
        self.empl = empl

    def __str__(self):
        desc = "This is student " + self.name + ", " + str(
            self.age) + ' years old studying at ' + self.uni + ' University.'
        return desc

    def casual_pay(self, hours_worked):
        rate_of_pay = 16.50
        if self.age >= 21:
            rate_of_pay += 4.50

        return rate_of_pay * hours_worked

    def is_teenager(self):
        return self.age < 20


def main(stud, suburb, hours_worked):
    for student in stud:
        if student.empl:
            if student.address == suburb:
                print("{}, Payment: {}".format(student.name, student.casual_pay(hours_worked)))


stud = [Student('Cleo', 21, 'Adelaide', 'Adelaide', 218918, True),
        Student('Jake', 20, 'Clovelly Park', 'Flinders', 218121, True),
        Student('Callum', 22, 'Blackwood', 'Flinders', 218958, True),
        Student('David', 24, 'Blackwood', 'Flinders', 218432, False),
        Student('Claudia', 26, 'Blackwood', 'Flinders', 218301, False),
        Student('Mona', 23, 'Royal Park', 'Adelaide', 218321, False),
        Student('Clay', 18, 'Clovelly Park', 'Flinders', 218900, True),
        Student('Amy', 21, 'Blackwood', 'Flinders', 218200, True),
        Student('William', 20, 'Clovelly Park', 'Adelaide', 218761, False),
        Student('Luka', 19, 'Royal Park', 'Adelaide', 218311, True)]
suburb = "Blackwood"
hours_worked = 10

main(stud, suburb, hours_worked)

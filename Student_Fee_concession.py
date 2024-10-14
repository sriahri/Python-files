class Student:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class Marks(Student):
    def __init__(self, maths, physics, chemistry, id, name):
        super().__init__(id, name)
        self.maths = maths
        self.physics = physics
        self.chemistry = chemistry


class Sports:
    def __init__(self, sports_marks):
        self.sports_marks = sports_marks


class Result(Marks, Sports):
    def __init__(self, maths, physics, chemistry, id, name, sports_marks):
        super().__init__(maths, physics, chemistry, id, name)
        self.sports_marks = sports_marks
        self.total_fees = 200000
        self.total = 0
        self.average = 0
        self.percentage = 0
        self.final_fees = 0

    def calculate(self):
        self.total = self.maths + self.physics + self.chemistry + self.sports_marks
        self.average = self.total / 4
        if self.average > 90:
            self.percentage = 50
        elif self.average > 80:
            self.percentage = 25
        elif self.average > 70:
            self.percentage = 10
        elif self.average > 60:
            self.percentage = 5
        else:
            self.average = 0

        self.final_fees = self.total_fees - (self.total_fees*self.percentage)/100

    def __str__(self):
        return '1. Total: {}\n2. Average: {}\n3. Percentage: {}\n4. Final fees: {}'.format(self.total, self.average, self.percentage, self.final_fees)


if __name__ == '__main__':
    id = input("Enter the student Id: ")
    name = input("Enter student name: ")
    maths = float(input("Enter maths marks: "))
    physics = float(input("Enter physics marks: "))
    chemistry = float(input("Enter chemistry marks: "))
    sports_marks = float(input("Enter sports marks: "))
    student = Result(maths, physics, chemistry, id, name, sports_marks)
    student.calculate()
    print(student)
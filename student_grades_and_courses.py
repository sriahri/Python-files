class Student:
    def __init__(self, name, courses, grades):
        self.name = name
        self.courses = courses
        self.grades = grades

    def __str__(self):
        return 'Name: {}, Courses: {}, Grades: {}\n'.format(self.name, self.courses, self.grades)


def displayStudentInfo(students):
    for i in students:
        print(i.__str__())


def displaySpecificCourseInfo(students, course):
    for i in students:
        if course in i.courses:
            print(i.__str__())


def transcriptInfo(students):
    for i in students:
        print('{}: {}'.format(i.name, i.grades))


def main():
    student_list = []
    student1 = Student('Jack', ['DBMS', 'OS', 'CN'], ['A', 'B', 'A'])
    student2 = Student('John', ['DS', 'OS', 'DAA'], ['A', 'B', 'A'])
    student3 = Student('Steve', ['DS', 'TOC', 'WT'], ['A', 'B', 'A'])
    student4 = Student('Jack', ['DBMS', 'TOC', 'CN'], ['A', 'B', 'A'])
    student_list.append(student1)
    student_list.append(student2)
    student_list.append(student3)
    student_list.append(student4)
    while True:
        print('1. Display Student information')
        print('2. Display list of students for a specific course')
        print('3. Display transcript information')
        print('4. end')

        choice = int(input('Enter your choice: '))
        if choice == 1:
            displayStudentInfo(student_list)
        elif choice == 2:
            course = input('Enter the course: ')
            displaySpecificCourseInfo(student_list, course)
        elif choice == 3:
            transcriptInfo(student_list)
        elif choice == 4:
            return


if __name__ == '__main__':
    main()

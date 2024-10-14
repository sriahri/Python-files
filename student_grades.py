def average_grade(student_grades):
    grade_sum = 0
    for student in student_grades:
        grade_sum += student.get('grade')

    return grade_sum / len(student_grades)


# the output of average_grade function for given example data: 58.0
def average_grade_of_male_students(student_grades):
    grade_sum = 0
    male_students = 0
    for student in student_grades:
        if student.get('gender') == 'male':
            grade_sum += student.get('grade')
            male_students += 1

    return grade_sum / male_students


# the output of average_grade_of_male_students function for given example data:
# 49.0


def maximum_grade_of_female_students(student_grades):
    maximum_grade = 0
    for student in student_grades:
        if student.get('gender') == 'female':
            if maximum_grade < student.get('grade'):
                maximum_grade = student.get('grade')
    return maximum_grade


# the output of maximum_grade_of_female_students function for given example data:
# 82


def calculate_and_add_letter_grades(student_grades, grade_table):
    for student in student_grades:
        letter_grade = [i for i in grade_table if grade_table[i][0] <= student['grade'] < grade_table[i][1]][0]
        student['letter_garde'] = letter_grade

    for student in student_grades:
        print(student)
    print()


# the student_grades after the execution of calculate_and_add_letter_grades
def sort_descending_order_by_grades(student_grades):
    res = sorted(student_grades, key=lambda x: x.get('grade'), reverse=True)
    for student in res:
        print(student)


student_grades = [{'name': 'Kathlyn Wakefield', 'gender': 'female', 'grade': 75},
                  {'name': 'Gerry Kinsey', 'gender': 'male', 'grade': 90},
                  {'name': 'Isaac Fortune', 'gender': 'male', 'grade': 8},
                  {'name': 'Elisa Christian', 'gender': 'female', 'grade': 35},
                  {'name': 'Christy Derrickson', 'gender': 'female', 'grade': 82}]
grade_table = {'A+': (90, 100),
               'A': (80, 89),
               'B+': (75, 79),
               'B': (70, 74),
               'C+': (65, 69),
               'C': (60, 64),
               'C-': (0, 59)}
print(average_grade(student_grades))
print()
print(average_grade_of_male_students(student_grades))
print()
print(maximum_grade_of_female_students(student_grades))
print()
calculate_and_add_letter_grades(student_grades, grade_table)
print()
sort_descending_order_by_grades(student_grades)

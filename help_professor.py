number_of_students = int(input("Enter the number of students: "))
students_scores = []
names = []
subjects = []
student_averages = []


def read_info(number_of_students):
    for i in range(number_of_students):
        names.append(input())
        list_of_subjects = []
        list_of_scores = []
        for j in range(5):
            subject, score = input().split()
            list_of_subjects.append(subject)
            while not -1 < float(score) < 111:
                print("Score is not valid!")
            list_of_scores.append(float(score))
        students_scores.append(list_of_scores)
        subjects.append(list_of_subjects)


def sort_scores(student_scores):
    for i in range(number_of_students):
        student_scores[i].sort()


def calculate_average(student_scores):
    for i in range(number_of_students):
        average = sum(student_scores[i]) / 5
        student_averages.append(average)


def display_info():
    print('Name\tScore1\tScore2\tScore3\tScore4\tScore5')
    for i in range(number_of_students):
        print('{}\t{}\t{}\t{}\t{}\t{}'.format(names[i], students_scores[i][0],
                                              students_scores[i][1], students_scores[i][2],
                                              students_scores[i][3], students_scores[i][4]))


read_info(number_of_students)
sort_scores(students_scores)
calculate_average(students_scores)
print()
display_info()
print()
print('Name\tAverage\tGPA')
for i in range(number_of_students):
    GPA = 'F'
    if student_averages[i] > 90:
        GPA = 'A'
    elif student_averages[i] > 80:
        GPA = 'B'
    elif student_averages[i] > 70:
        GPA = 'C'
    elif student_averages[i] > 60:
        GPA = 'D'
    elif student_averages[i] > 50:
        GPA = 'E'
    print('{}\t{}\t{}'.format(names[i], student_averages[i], GPA))

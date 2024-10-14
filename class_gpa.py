if __name__ == '__main__':
    print('GPA Calculator')
    # Prompt the number of classes
    number_of_classes = int(input('Enter total classes: '))
    grades = []  # List to store grades
    # For loop to prompt for grades
    for i in range(1, number_of_classes + 1):
        grade = input('Enter grade for class {}: '.format(i))
        # While loop to check the grade is numeric or not
        while not grade.isnumeric():
            print('Percentage grades only please!')
            grade = input('Enter grade for class {}: '.format(i))
        grades.append(int(grade))

    # Average of all grades
    average = sum(grades) / len(grades)
    # GPA
    gpa = (average / 20) - 1
    # If GPA is less than 0, then it is set to 0
    if gpa < 0:
        gpa = 0

    # Printing up to 2 decimal places for GPA
    print('Your GPA: {:.2f}'.format(gpa))

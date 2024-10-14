john_grades = [3, 3.78, 2.87, 3.2, 4, 3.43]
smith_grades = [1.2, 4, 3, 3.1, 1.7, 3.4]
ani_grades = [4, 4, 1.7, 3, 2.4, 3.1]
greg_grades = [3.1, 3.5, 3.9, 2.8, 4, 2.7]

john_grades_average = sum(john_grades)/len(john_grades)
smith_grades_average = sum(smith_grades)/len(smith_grades)
ani_grades_average = sum(ani_grades)/len(ani_grades)
greg_grades_average = sum(greg_grades)/len(greg_grades)

john_failed = 0
for grade in john_grades:
    if grade < 2:
        john_failed += 1

smith_failed = 0
for grade in smith_grades:
    if grade < 2:
        smith_failed += 1

ani_failed = 0
for grade in ani_grades:
    if grade < 2:
        ani_failed += 1

greg_failed = 0
for grade in greg_grades:
    if grade < 2:
        greg_failed += 1
print()
print('Grades for John -> Average:', john_grades_average)
print('The number of courses failed by John:', john_failed)
print('Grades for Smith -> Average:', smith_grades_average)
print('The number of courses failed by Smith:', smith_failed)
print('Grades for Ani -> Average:', ani_grades_average)
print('The number of courses failed by Ani:', ani_failed)
print('Grades for Greg -> Average:', greg_grades_average)
print('The number of courses failed by Greg:', greg_failed)

grade_averages = {'john': john_grades_average, 'smith': smith_grades_average, 'ani': ani_grades_average,
                  'greg': greg_grades_average}
result = sorted(grade_averages, key=lambda x: grade_averages[x], reverse=True)
print('Places:')
print('{} is at first place.'.format(result[0].title()))
print('{} is at second place.'.format(result[1].title()))
print('{} is at third place.'.format(result[2].title()))
print('{} is at fourth place.'.format(result[3].title()))

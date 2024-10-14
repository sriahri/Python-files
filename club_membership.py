print('''1. Standard adult
2. Child (age 12 and under)
3. Student
4. Senior citizen (age 65 and over)''')
adult_amount = 40
child_amount = 20
student_amount = 25
senior_citizen_amount = 30
member_type = int(input('Enter the type of person you are from the above: '))
membership_amount = 0
if member_type == 1:
    membership_amount += adult_amount
elif member_type == 2:
    membership_amount += child_amount
elif member_type == 3:
    membership_amount += student_amount
else:
    membership_amount += senior_citizen_amount

no_lessons_amount = 0
yoga_lessons_amount = 10
personal_trainer_amount = 50
yoga_and_personal_trainer_amount = 60

print('''0. No lessons
1. Yoga lessons
2. Personal trainer
3. Yoga and Personal trainer''')

optional_services = int(input('Please select any optional services required: '))
if optional_services == 0:
    membership_amount += no_lessons_amount
elif optional_services == 1:
    membership_amount += yoga_lessons_amount
elif optional_services == 2:
    membership_amount += personal_trainer_amount
elif optional_services == 3:
    membership_amount += yoga_and_personal_trainer_amount

membership_duration = int(input('Enter the number of months you want to take the membership: '))

if 1 <= membership_duration <= 3:
    membership_amount = membership_amount
elif 4 <= membership_duration <= 6:
    membership_amount = membership_amount * 0.95
elif 7 <= membership_duration <= 9:
    membership_amount = membership_amount * 0.92
elif membership_duration >= 10:
    membership_amount = membership_amount * 0.9

print()
print('The monthly fee for the opted membership is {}'.format(membership_amount))
total_amount = membership_amount * membership_duration
print()
print('The total amount due for the membership term is {}'.format(total_amount))

actual_answers = ['B','D','A','A','B','A','B','A','C','D','B','C','D','A','D','C','C','B','D','A']
f = open('E:\idledoc\inputfile.txt')
test_list = f.readlines()
for i in range(20):
    test_list[i] = test_list[i][0]
print(test_list)
correct_answers = 0
correct_questions = []
wrong_questions = []
for i in range(20):
    if actual_answers[i] == test_list[i]:
        correct_answers += 1
        correct_questions.append(i+1)
    else:
        wrong_questions.append(i+1)

if correct_answers >= 15:
    print('The person has passed the exam.')
else:
    print('The person has failed the exam.')

print('The number of correct answers are',correct_answers)
print('The correct answered questions are',correct_questions)
print('The number of questions answered wrong are',20-correct_answers)
print('The questions which are answered wrong are',wrong_questions)
if __name__ == '__main__':
    file = open('QA_Pairs.txt', 'r')
    lines = list(file.readlines())
    i = 0
    questions = []  # All the questions
    answers = []  # All the answers

    for i in lines[::2]:
        questions.append(i)
    for i in lines[1::2]:
        answers.append(i)
    print('The number of Q&A pairs is {}'.format(len(questions)))
    print(questions)
    print(answers)
    dict_questions = {}  # Questions with count of occurrence
    dict_answers = {}  # Answers with count of occurrence
    for i in questions:
        if i not in dict_questions:
            dict_questions[i] = 1
        else:
            dict_questions[i] += 1

    for i in answers:
        if i not in dict_answers:
            dict_answers[i] = 1
        else:
            dict_answers[i] += 1

    overlapping = []  # Overlapping questions and answers
    unique = []  # Unique questions and answers
    for i in range(len(questions)):
        if dict_questions[questions[i]] > 1 or dict_answers[answers[i]] > 1:
            overlapping.append(questions[i])
            overlapping.append(answers[i])
        else:
            unique.append(questions[i])
            unique.append(answers[i])
    overlapping_file = open('Overlapping.txt', 'w')
    unique_file = open('unique_QA_Pairs.txt', 'w')
    overlapping_file.writelines(overlapping)
    unique_file.writelines(unique)
    overlapping_file.close()
    unique_file.close()

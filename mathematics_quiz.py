import random

print("Welcome to the mathg program.")
print("Quit anytime by typing 'q' or 'Q'.")
keep_asking_questions = True
question = None
solution = None
number_of_correct_answers = 0
number_of_incorrect_answers = 0
score = 0
total_questions = 0
while keep_asking_questions:
    # Generate a random math question and its solution
    first_num = random.randint(0, 9)
    second_num = random.randint(0, 9)
    operator = random.randint(0, 3)
    if operator == 0:
        # Create multiplication question and solution
        solution = first_num * second_num
        question = "%d x %d = " % (first_num, second_num)
    elif operator == 1:
        # Create division question and solution
        while second_num == 0:
            second_num = random.randint(0, 9)
            solution = first_num * second_num
            (solution, first_num) = (first_num, solution)
            question = "%d / %d = " % (first_num, second_num)
    elif operator == 2:
        # Create addition question and solution
        solution = first_num + second_num
        question = "%d + %d = " % (first_num, second_num)
    else:  # Create subtraction question and solution
        while first_num == 0:
            first_num = random.randint(0, 9)
            solution = first_num + second_num
            (solution, first_num) = (first_num, solution)
            question = "%d - %d = " % (first_num, second_num)
    # Display the question and get valid response
    response_is_not_valid = True
    response = None
    while response_is_not_valid:
        print(question, '?')
        response = input("> ")
        # Check if response is valid
        if response.isdigit() or response == 'q' or response == 'Q':
            response_is_not_valid = False
        else:
            print("That was an invalid response. Enter a number or 'q' or 'O' to quit.")
    # Check correctness of user's response
    if response == 'q' or response == '':
        keep_asking_questions = False
    else:
        if int(response) == solution:
            print('Correct!')
            number_of_correct_answers += 1
            score += 1
            print('')
        else:
            print("Incorrect! %s '%d" % (question, solution))
            number_of_incorrect_answers += 1
    total_questions += 1

if score > 0:
    print('You answered %d out of %d questions correctly' %(number_of_correct_answers, total_questions))
print("Exiting the mathq program.")

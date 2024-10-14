"""Mastermind
this is a simulation of the game mastermind
there is a secret combination of four colored pegs and then a series of guesses at that combination
correctness is evaluated by a black peg indicating that there is a
correctly colored peg in a correct position
a white peg indicating that there is a correctly colored peg in an incorrect position

combinations and guesses in this program will be indicated by four letter strings
where each letter is the initial of a color:
red, yellow, blue, green, purple, white

there will be some randomness in producing solutions to guess at or to make random guesses
"""
import random

'''this is a list of the valid colors for general use
'''
colors = ['R', 'Y', 'B', 'G', 'P', 'W']

'''some functions relating to generating and validating combinations'''


def is_valid(combination):
    """identifies whether combination is valid: four letters from the list defines above
    returns true or false accordingly"""
    if len(combination) != 4:
        return False
    else:
        valid = True
    for letter in combination:
        if letter not in colors:
            valid = False
    return valid


def random_combination():
    """a random combination of four letters for this simulation
    random.select() is NOT chosen, because it disallows duplicates"""
    return random.choice(colors) + random.choice(colors) + random.choice(colors) + random.choice(colors)


def input_combination():
    """asks the user for a combination, and continues to ask if the input is invalid"""
    combination = input('What would you like to guess? ')
    while not is_valid(combination):
        print('Guess must be four letters from RYBGPW')
        combination = input('Try again: ')
    return combination


def all_combinations():
    """generates a list of all valid combinations"""
    combo_list = []
    for first in colors:
        for second in colors:
            for third in colors:
                for fourth in colors:
                    combo_list.append(first + second + third + fourth)
    return combo_list


'''functions to see if the check_guess function works correctly'''


def test_check_guess(guess, answer, result, message):
    response = check_guess(guess, answer)
    if response == result:  # it worked!\
        return True
    elif len(response) != 2:
        print('Did not get black and white pegs comparing ', guess, 'to', answer)
        return False
    else:
        print('Got response of', response, 'comparing', guess, 'to', answer)
        print('correct result would be', result, '--', message)
        return False


def test_checker():
    test_check_guess('RBBB', 'RGGG', (1, 0), 'cannot find the black peg')
    test_check_guess('BBBR', 'GGGR', (1, 0), 'cannot find the black peg')
    test_check_guess('RRBB', 'RRGG', (2, 0), 'did you find both black pegs?')
    test_check_guess('RBBR', 'RGGR', (2, 0), 'two black pegs cannot also be white')
    test_check_guess('RRRR', 'RRRR', (4, 0), 'four black pegs cannot also be white')
    test_check_guess('RRBB', 'GGRR', (0, 2), 'only one white peg per guess peg')
    test_check_guess('RBYW', 'BYWG', (0, 3), ' must be able to find all the colors')
    test_check_guess('RBYW', 'WRBY', (0, 4), ' must be able to find all the colors')
    test_check_guess('RBYW', 'RYWB', (1, 3), ' do not count black pegs as white also')


# student work begins below

def check_guess(guess, answer):
    """compares a guessed combination with the right answer
    one black peg for each correct color in correct location one white peg for each correct
    color in incorrect location"""
    answer_copy = list(answer)  # make editable copies of each
    guess_copy = list(guess)
    # first examine each position to see if colors match (black pegs)
    # replacing guessed letters with blank pegs when there is a match
    # eliminate those pegs from the guess to avoid extra white pegs

    black = 0
    white = 0
    remaining_guess = []
    remaining_answer = []

    # Count black pegs (correct color in correct position)
    for i in range(len(guess)):
        if guess[i] == answer[i]:
            black += 1
        else:
            remaining_guess.append(guess[i])
            remaining_answer.append(answer[i])

    # Count white pegs (correct color in incorrect position)
    for color in remaining_guess:
        if color in remaining_answer:
            white += 1
            remaining_answer.remove(color)

    return black, white
    # return the number of pegs


def user_guesses():
    """ a game of mastermind where the keyboard user
    tries to guess a combination chosen by the computer"""
    '''pick an answer, then request and evaluate a first guess
    if the guess is wrong report on results and evaluate next guess
    repeating until there is a correct guess'''
    answer = random_combination()
    print("Try to guess my combination!")

    while True:
        guess = input_combination()
        black, white = check_guess(guess, answer)

        print(f"{black} pegs (correct color in correct location)")
        print(f"{white} pegs (correct color in incorrect location)")

        if black == 4:
            print("You got it!")
            break
    print('You got it!')


def computer_guesses():
    """a game of mastermind where the computer guesses at a combination chosen by the keyboard user"""
    # start with all possible combinations
    # if the answer is not yet known

    # pick a guess and have it evaluate it

    # eliminate from consideration all combinations that cant
    # be correct (multiple calls to the check_guess function)

    # report the solution when found
    pool = all_combinations()
    answer = input_combination()

    while pool:
        guess = random.choice(pool)
        black, white = check_guess(guess, answer)

        print(f"My guess is {guess}")
        print(f"How many black pegs (correct color in correct location)? {black}")
        print(f"How many white pegs (correct color in incorrect location)? {white}")

        if black == 4:
            print("I think I have it! Your combination is", guess)
            break

        pool = [comb for comb in pool if check_guess(comb, guess) == (black, white)]


# the 'main; part of this code just alternates
# between the player guessing and the computer guessing
# once the check_guess function is all correct
# the following function call will have no output
test_checker()

print('Welcome to Mastermind!')
yesno = 'y'
while yesno in ['y', 'Y']:
    print('Try to guess my combination!')
    user_guesses()
    print('My turn, to guess at yours!')
    computer_guesses()
    yesno = input('Play again? ')

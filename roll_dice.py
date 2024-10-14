import random

MIN_ROLL = 1
MAX_ROLL = 6
MIN_BET = 5


def roll_one_die() -> int:
    """ simulates the roll of a single dice between MIN_ROLL and MAX_ROLL
    inclusive and returns the value.
    No examples due to behaviour being dependent on randomly generated values.
    """
    # generates a random number between MIN_ROLL and MAX_ROLL inclusive
    die = random.randint(MIN_ROLL, MAX_ROLL)

    # for testing to allow you to enter the dice roll you want at the keyboard
    # comment out the line above and uncomment this line:
    # die = int(input('enter a simulated dice roll\n'))

    return die


def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()


def play_again():
    choice = input('Do you want to make a bet?  Enter yes if you do: ')
    if choice.lower() == 'yes':
        return True
    else:
        return False


def get_guess():
    guess = int(input('Enter an integer between 1 and 6 inclusive: '))
    while not is_integer(guess):
        guess = int(guess)
        while guess < 1 or guess > 6:
            guess = int(input('Enter an integer between 1 and 6 inclusive: '))
    return guess


def get_bet(MAXIMUM):
    bet_amount = int(input('Enter an integer between 5 and {} inclusive: '.format(MAXIMUM)))
    while bet_amount < MIN_BET or bet_amount > MAXIMUM:
        bet_amount = int(input('Enter an integer between 5 and {} inclusive: '.format(MAXIMUM)))
    print('You bet $', bet_amount)
    return bet_amount


def roll_dice(guessed_number):
    count = 0

    number = roll_one_die()
    print('Dice roll {}: {}'.format(0, number))
    if number == guessed_number:
        count += 1
    number = roll_one_die()
    print('Dice roll {}: {}'.format(1, number))
    if number == guessed_number:
        count += 1
    number = roll_one_die()
    print('Dice roll {}: {}'.format(2, number))
    if number == guessed_number:
        count += 1
    return count


def compute_winnings(matches, amount):
    if matches == 1:
        return amount
    elif matches == 2:
        return amount * 2
    elif matches == 3:
        return amount * 10
    elif matches == 0:
        return amount * -1


def play_one_round(amount):
    guess = get_guess()
    matches = roll_dice(guess)
    return compute_winnings(matches, amount)


def play_game(amount):
    print('You have ${} to play with'.format(amount))
    play_again_choice = True
    while amount > MIN_BET and play_again_choice:
        bet_amount = get_bet(amount)
        gain_lost_amount = play_one_round(bet_amount)
        amount += gain_lost_amount
        print('You have ${} in your bankroll'.format(amount))
        play_again_choice = play_again()

    print('You have ${} in your bankroll'.format(amount))


play_game(400)

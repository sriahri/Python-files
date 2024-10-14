import random


def guess(limit, number):
    random_number = random.randint(1, number)
    try:
        while limit > 0:
            guess_number = int(input("What is your guess? "))
            limit -= 1
            if random_number == guess_number:
                print('Congratulations, You got it correct!')
                break
            elif guess_number > random_number:
                print('Your guess greater than the number.')
                print('You have {} guess(es) left'.format(limit))
            else:
                print('Your guess is less than the number.')
                print('You have {} guess(es) left'.format(limit))
        print('Game Over....!')
        print('The random number was {}'.format(random_number))

    except ValueError:
        print('Only integers are allowed!')


def easy():
    print('You are to guess number between 1 and 10 and you have 6 guesses')
    guess(6, 10)


def medium():
    print('You are to guess number between 1 and 20 and you have 4 guesses')
    guess(4, 20)


def hard():
    print('You are to guess number between 1 and 50 and you have 3 guesses')
    guess(3, 50)


def play_again():
    again = input('Do you want to play again? Yes/No')
    if again.lower() == 'yes:':
        welcome()
    elif again.lower() == 'no':
        print('Thanks for playing....!')
    else:
        print('Please provide a valid input.')
        play_again()


def welcome():
    print('Welcome to the game!')
    difficulty = input('Choose the level of difficulty (Easy)/(Medium)/(Hard)? ')
    if difficulty.lower() == 'easy':
        easy()
        play_again()
    elif difficulty.lower() == 'medium':
        medium()
        play_again()
    elif difficulty.lower() == 'hard':
        hard()
        play_again()
    else:
        print('Please provide a valid input.')
        welcome()


if __name__ == '__main__':
    welcome()

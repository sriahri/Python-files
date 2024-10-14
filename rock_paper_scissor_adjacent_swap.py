def printOutcome(user_selection, computer_selection):
    user_selection = user_selection.lower()
    computer_selection = computer_selection.lower()
    if user_selection == computer_selection:
        print('A tie')
    elif user_selection == 'rock' and computer_selection == 'paper':
        print('HAL wins!')
    elif user_selection == 'rock' and computer_selection == 'scissors':
        print('You win')
    elif user_selection == 'paper' and computer_selection == 'rock':
        print('You win')
    elif user_selection == 'paper' and computer_selection == 'scissors':
        print('HAL wins!')
    elif user_selection == 'scissors' and computer_selection == 'paper':
        print('You win')
    elif user_selection == 'scissors' and computer_selection == 'rock':
        print('HAL wins!')


def RPS_main():
    while True:
        import random
        print('Rock, Paper, Scissors!')
        rock_paper_scissors = ['Rock', 'Paper', 'Scissors']
        print("Make your selection...")
        choice = int(input('(1) rock, (2) Scissors, (3) Paper? '))
        while choice < 1 or choice > 3:
            print('Invalid selection! Try again.')
            print("Make your selection...")
            choice = int(input('(1) rock, (2) Scissors, (3) Paper? '))
        user_selection = rock_paper_scissors[choice - 1]
        hal_selection = rock_paper_scissors[random.randint(1, 3)-1]
        print('You: {}\nHAL: {}'.format(user_selection, hal_selection))
        printOutcome(user_selection, hal_selection)
        play = input('Want to play again?(Y/N): ')
        if play == 'N' or play == 'n':
            break
        elif play == 'Y' or play == 'y':
            pass
        else:
            print('Invalid choice! and proceeding to play')


def swapAdjacentElements(alist):
    for i in range(0, len(alist)-1, 2):
        alist[i], alist[i + 1] = alist[i + 1], alist[i]


def SAEMain():
    string = input('Enter the characters separated by spaces: ')
    list_of_chars = string.split()
    print('Initial list:')
    print(list_of_chars)
    print('String Version:')
    print(''.join(list_of_chars))
    swapAdjacentElements(list_of_chars)
    print('Modified list:')
    print(list_of_chars)
    print('String Version:')
    print(''.join(list_of_chars))


if __name__ == '__main__':
    RPS_main()
    SAEMain()

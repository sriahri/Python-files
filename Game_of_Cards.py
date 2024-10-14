import random
import time
def determineWinner(winsPlayer1, winsPlayer2):
    if winsPlayer1 > winsPlayer2:
        print('Player 1 wins the Game.')
    elif winsPlayer2 > winsPlayer1 :
        print('Player 2 wins the Game.')
    else:
        print("The game ends in a Tie.")

num_rounds = 10
wins_player1 = 0
wins_player2 = 0
for i in range(10):
    print('------- ROUND',(i+1),'-------')
    card1 = random.randint(0,10)
    card2 = random.randint(0,10)
    if card1 > card2:
        print('Player 1 wins the round.')
        wins_player1 += 1
    elif card2 > card1:
        print('Player 2 wins the round.')
        wins_player2 += 1
    else:
        print('This round is a tie.')
    print('Wins by player 1 is',wins_player1)
    print('Wins by player 2 is',wins_player2)
    print()
    time.sleep(2)
determineWinner(wins_player1, wins_player2)
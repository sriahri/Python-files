import random


# make sure to have function comments
def roll(numSides):
    # check to see if numSides is between 1 and 64
    if 1 <= numSides <= 64:
        return numSides
        # return the random roll
    else:
        return -1


# build a tossCoin() function
# make sure to have function comments
def tossCoin():
    # create a random number between 0 and 1.
    # if random number==0:
    # return "heads"
    # else:
    # return "tails"
    choice = random.randint(0, 1)
    return "heads" if choice == 0 else "tails"


# create 2 players and call roll() for each
# these are the scores.

sides = random.randrange(1, 64)
player1 = roll(sides)
sides = random.randrange(1, 64)
player2 = roll(sides)

if player2 == -1 or player1 == -1:
    print("dice sides aren't between 1 and 64")


elif player2 == player1:
    toss = tossCoin()
    if toss == 0:
        print("Player 1 wins")
    else:
        print("Player 2 wins")

elif player2 > player1:
    print("Player 1 : {}".format(player1))
    print("Player 2 : {}".format(player2))
    print('Player 2 wins')

else:
    print("Player 1 : {}".format(player1))
    print("Player 2 : {}".format(player2))
    print("player 1 wins")
# create a conditional to check to see who wins.
# build an if that checks to see if player1 or player2==-1
# print some kind of statement saying dice sides aren't between 1 and 64
# else if to check if player 1 wins
# print player 1's score and player 2's score and say who wins
# else if to check if player 2 wins
# mimic the print statement above
# else:
# call tossCoin() and store it as a variable
# if tossCoin()=="heads":
# decide who wins
# else:
# say who else wins.

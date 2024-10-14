# From random module importing the required 
# functions randint and randrange
from random import randint, randrange
# From math import cos
from math import cos

def racer1Move():
    # Randrange take in the input start, stop and the step value.
    # Since we need only 4 or 8 we use it this way. 
    # So that the value 4 or 8 is returned.
    steps = randrange(4,9,4)
    return steps

def racer2Move():
    # Random integer between 2 and 10 both inclusive.
    steps = randint(2,11)
    return steps

def racer3Move():
    # First we try to determine which one to be used for steps either 0 or 1.
    choice = randint(0,2)
    if choice == 0:
        steps = randint(0,10)
    else:
        steps = 7*cos(7)
    return steps

def racer4Move():
    # Since it is said that the racer must move atleast 
    # one unit so that the range is consisdered to be 0 to 5.
    # Beacuse 2**6 is 64 where 45/64 will be less than 1.
    turns = randint(0,6)
    steps = 45//(2**turns)
    return steps

racer1 = 0
racer2 = 0
racer3 = 0
racer4 = 0
while racer1 < 100 and racer2 < 100 and racer3 < 100 and racer4 < 100:
    racer1 += racer1Move()
    racer2 += racer2Move()
    racer3 += racer3Move()
    #racer4 += racer4Move()
if racer1 >= 100:
    print('Racer 1 won the race')
elif racer2 >= 100 :
    print('Racer 2 won the race')
elif racer3 >= 100:
    print('Racer 4 won the race')
elif racer4 >= 100:
    print('Racer 4 won the race')
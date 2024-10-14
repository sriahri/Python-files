import random
name = input("Please enter your first name: ")  
# Generating random numbers between 2 and 14
face_card_1 = random.randint(2,14)
face_card_2 = random.randint(2,14)
face_card_3 = random.randint(2,14)
# Generating random numbers between 1 and 4
suite_1 = random.randint(1,4)
suite_2 = random.randint(1,4)
suite_3 = random.randint(1,4) 
# Generating random number between 7 and 45
computer_score = random.randint(7,45) 
# Adding up all the face cards
player_score = face_card_1 + face_card_2 + face_card_3
# Checking whether all the suites are equal or not.
if suite_1 == suite_2 and suite_1 == suite_3 :
    player_score += 3
# Checking whether any two if the suites are equal or not.
elif suite_1 == suite_2 or suite_1 == suite_3 or suite_2 == suite_3 :
    player_score += 2
else:
    player_score += 1
print(name,'total is',player_score)
print('Computer total is',computer_score)
# Comparing computer and player score.
if player_score > computer_score :
    print(name,'Congragulations,','you are the winner.')
elif player_score == computer_score :
    print('The game is tied')
else:
    print('Sorry',name,'you have lost to your opponent.')
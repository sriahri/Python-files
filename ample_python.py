def Q2(Q1):
    for character in Q1:  # Loop through each character
        if not character.isspace():  # Print only if it is not space
            print(character)


def Q3(Q1):
    for character in Q1:
        if not character.isspace():
            print('A')


Q1 = "Data Science for all"
print('Function call Q2')
Q2(Q1)
print('Function call Q3')
Q3(Q1)

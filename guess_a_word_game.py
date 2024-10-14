import random
import string

# Contains 7 random lower case letters in a string
random_letters = ''.join(random.choices(string.ascii_lowercase, k=7))
print('The random letters are ', random_letters)
chances = 3
score = 0
for i in range(chances):
    # Prompt the user
    word = input('Enter a word that can be spelled with the random letters: ')
    flag = True
    while len(word) < 3:
        # continuously check the word length and prompt
        print('Word must be three characters in length')
        word = input('Enter a word that can be spelled with the random letters: ')
    # Check the word can be spelled with random letters or not
    for letter in word:
        if letter not in random_letters:
            flag = False

    # If the word cannot be spelled with random letters
    if not flag:
        print('Word cannot be spelled with the random letters')

    # If the word can be spelled with random letters
    if flag:
        score += len(word) * 10

    # Print the score after each turn
    print('After turn {}: score is {}'.format(i + 1, score))

# Print the score after all turns
print('After all turns: score is {}'.format(score))

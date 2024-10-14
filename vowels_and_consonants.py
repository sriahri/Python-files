# Read input string from the user
input_string = input('Enter a string: ')
# List of vowels
vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
vowels_count = 0
consonant_count = 0
# Iterate through the string and find the vowels and consonant count
for i in input_string:
    if i.isalpha():
        if i in vowels:
            vowels_count += 1
        else:
            consonant_count += 1
print('Number of vowels in the string are {}'.format(vowels_count))
print('Number of consonants in the string are {}'.format(consonant_count))

new_string = ''
# Replace all the consinants with @
for i in input_string:
    if i.isalpha():
        if i not in vowels:
            new_string += '@'
        else:
            new_string += i
print('New string is {}'.format(new_string))
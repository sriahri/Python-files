lower_alphabet_string = ''

for i in range(0, 26):
    lower_alphabet_string += chr(ord('a') + i)

letter = input('Enter starting letter: ')
step = -1
res = ''
if len(letter) > 1 or not letter.isalpha():
    print('You must enter one letter')

else:
    step = int(input('Enter step: '))
    if step == 0:
        print('Step cannot be 0')
    else:
        letter = letter.lower()
        i = lower_alphabet_string.find(letter)
        res = ''.join(lower_alphabet_string[i::step])
        print('Resulting substring is:', res)

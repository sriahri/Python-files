sentence = input('Enter the sentence: ')
special_symbols_count = 0
special_symbols = {}
for letter in sentence:
    if not (letter.isalpha() or letter == ' '):
        special_symbols_count += 1
        if letter in special_symbols:
            special_symbols[letter] += 1
        else:
            special_symbols[letter] = 1

if special_symbols_count == 0:
    print('NONE')
else:
    print('The number of special symbols are ', special_symbols_count)
    print('The special symbols that are present along with their count are: ')
    for symbol, count in special_symbols.items():
        print('{}: {}'.format(symbol, count))

characters = [0] * 26
for letter in sentence:
    if letter.isalpha():
        if letter.isupper():
            characters[ord(letter) - ord('A')] += 1
        else:
            characters[ord(letter) - ord('a')] += 1

print('The character distribution is: ')
i = 0
for count in characters:
    if count != 0:
        print('{} or {}: {}'.format(chr(i + ord('A')), chr(i + ord('a')), count))
    else:
        print('{} or {}: None'.format(chr(i + ord('A')), chr(i + ord('a'))))

    i += 1

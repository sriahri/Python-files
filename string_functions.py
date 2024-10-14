def first_last(s):
    return s[0], s[-1]


def char_types(s):
    vowels_count = 0
    consonants_count = 0
    for i in s:
        if i.isalpha():
            if i in ['a', 'e', 'i', 'o', 'u', 'y', 'A', 'E', 'I', 'O', 'U', 'Y']:
                vowels_count += 1
            else:
                consonants_count += 1
    return vowels_count, consonants_count


def char_symbol_number(s):
    characters_count = 0
    symbols_count = 0
    numbers_count = 0

    for i in s:
        if i.isalpha():
            characters_count += 1
        elif i.isnumeric():
            numbers_count += 1
        else:
            symbols_count += 1
    return characters_count, symbols_count, numbers_count


if __name__ == '__main__':
    sentence = 'May the Force be with you!'
    first_char, last_char = first_last(sentence)
    number_of_vowels, number_of_consonants = char_types(sentence)
    print('First and last in "{}":{}'.format(sentence, first_char + last_char))
    print('In that sentence {} the number of vowels is {} and the number of consonants is {}'
          .format(sentence, number_of_vowels, number_of_consonants))

    sentence = 'I am 1 with the Force, not 2...'
    number_of_characters, number_of_symbols, number_of_numbers = char_symbol_number(sentence)
    print('In the sentence "{}" the number of letters is {}, symbols is {} and numbers is {}'
          .format(sentence, number_of_characters, number_of_symbols, number_of_numbers))

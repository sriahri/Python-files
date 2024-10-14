def count_characters_non_white(text):
    text = text.replace(' ', '')
    return len(text)


def position_6th(text):
    if len(text) < 6:
        print('Too Short')
        return
    return text[5].upper()


def uppercase_quote(text):
    return text.upper()


def last_word_repeat(text):
    import random
    words = text.split()
    last_word = words[-1]
    repeat_count = random.randint(3, 7)
    return last_word * repeat_count


def count_dictionary(text):
    words = text.split()
    result_dict = {}
    for word in words:
        if word in result_dict:
            result_dict[word] += 1
        else:
            result_dict[word] = 1
    return result_dict


if __name__ == '__main__':
    print('Welcome to the String Processing Program!')
    while True:
        quote = input('Please enter your favorite quote from a book:\n')
        print('Based on our processing, your favorite quote contains {} characters, not including spaces!'
              .format(count_characters_non_white(quote)))
        print('Here is the letter in the 6th position of your quote:\n', position_6th(quote))
        print('Here is the quote read by someone yelling:')
        print(uppercase_quote(quote))
        print(last_word_repeat(quote))
        print('Here are all the words in your quote and how often they appear:')
        print('--------WORD COUNT--------')
        result = count_dictionary(quote)
        for key, value in result.items():
            print('{}.............{}'.format(key, value))
        print("That's all the processing we have for you today! Do you want to do that again?")
        choice = input()
        if choice.lower() == 'no':
            break

    print('Thanks for sharing your favorite book quote!')

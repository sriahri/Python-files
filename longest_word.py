def longest_word(words):
    result = ''
    for word in words:
        if len(word) > len(result):
            result = word

    return result


if __name__ == '__main__':
    words = ['we', 'know', 'how', 'to', 'select', 'extremes']
    print(longest_word(words))

    words = ['we', 'already', 'know', 'how']
    print(longest_word(words))

    words = ['really?']
    print(longest_word(words))

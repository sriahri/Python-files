def is_word_there(text, word):
    # Convert the text to lowercase for case insensitive search.
    text = text.lower().strip()
    word = word.lower().strip()
    words = text.split()
    if word in words:
        return 1
    else:
        return -1


def count_word(text, word):
    # Convert the text to lowercase for case insensitive search.
    text = text.lower().strip()
    word = word.lower().strip()
    words = text.split()
    count = 0
    for find_word in words:
        if find_word == word:
            count += 1
    return count


def get_area_circle(r):
    pi = 3.1415
    return pi * r * r


if __name__ == '__main__':
    print(is_word_there('NJ is a great a place to live', 'Great'))
    print(is_word_there('NJ is a great a place to live', 'New York'))
    print(count_word('Montclair is located in NJ. MOntclair is a great place to live', 'Montclair'))
    print(count_word('Montclair is located in NJ. MOntclair is a great place to live', 'Verona'))
    print(get_area_circle(3))
    print(get_area_circle(1))
def countByLength(words):
    sorted_words = sorted(words, key = len, reverse=True)
    count_dict = {}
    for word in words:
        length = len(word)
        if length in count_dict:
            count_dict[length] += 1
    for i in sorted_words[:21]:
        print(i)
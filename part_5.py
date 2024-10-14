from itertools import permutations


def possible_combinations(name):
    file = open("dictionary.txt", "r")
    lines = file.readlines()
    words = []
    for i in lines:
        words.append(i.strip("\n"))
    combinations = permutations(name)
    for i in combinations:
        word = "".join(i)
        if word in words:
            print("Found:{}".format(word))


possible_combinations("tac")

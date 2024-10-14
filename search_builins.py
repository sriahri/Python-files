import time

list_example = [i for i in range(1, 1000000)]
tuple_example = tuple(i for i in range(1, 1000000))
set_example = set(i for i in range(1, 1000000))
sentence = ''.join(list(map(str, list_example)))


def search_builtin(builtin_type):
    for i in builtin_type:
        if i == -1:
            return 'Found'


def search_string(sentence):
    for i in sentence:
        if i == '-1':
            return 'Found'


if __name__ == '__main__':
    start = time.time()
    search_builtin(list_example)
    print("Time taken for list {}".format(time.time() - start))
    start = time.time()
    search_builtin(tuple_example)
    print("Time taken for tuple {}".format(time.time() - start))
    start = time.time()
    search_builtin(set_example)
    print("Time taken for set {}".format(time.time() - start))
    start = time.time()
    search_string(sentence)
    print("Time taken for string {}".format(time.time() - start))

def getAnagrams(word):
    getAnagramHelper("", word)


def getAnagramHelper(a, b):
    if len(b) <= 1:
        print(a + b)

    else:
        for i in range(len(b)):
            string1 = b[i:i + 1]
            string2 = b[0:i]
            string3 = b[i + 1:]
            getAnagramHelper(a + string1, string2 + string3)


if __name__ == '__main__':
    getAnagrams("python")

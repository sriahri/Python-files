from math import factorial
from collections import Counter


def calculate(a, b):
    if len(a) == len(b):
        list(a).sort()
        list(b).sort()
        if a == b:
            return True
    return False


def findSimilar(a, b):
    d1 = Counter(a)
    d2 = Counter(b)
    similar = calculate(a, b)
    if similar:
        if '0' in a:
            c = a.count('0')
            res = factorial(len(a) - 1) * (len(a) - c)
        else:
            res = factorial(len(a))

    else:
        if '0' in b:
            c = b.count('0')
            res = factorial(len(b) - 1) * (len(b) - c)
        else:
            res = factorial(len(b))
    for i in d2.keys():
        res = res//d2[i]
    return res


print(findSimilar('112', '121'))
print(findSimilar('11', '223'))
print(findSimilar('1234', '2341'))

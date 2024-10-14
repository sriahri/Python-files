import math

MAX_DIGITS = 6


def getValue(Str, i, m):
    if i + m > len(Str):
        return -1
    value = 0

    for j in range(m):
        c = (ord(Str[i + j]) -
             ord('0'))
        if c < 0 or c > 9:
            return -1
        value = value * 10 + c
    return value


def findMissingNumber(Str):
    for m in range(1, MAX_DIGITS + 1):

        n = getValue(Str, 0, m)
        if n == -1:
            break
        missingNo = -1

        fail = False
        i = m
        while i != len(Str):
            if (missingNo == -1) and (getValue(Str, i, 1 + int(math.log10(n + 2))) == n + 2):
                missingNo = n + 1
                n += 2

            elif getValue(Str, i, 1 + int(math.log10(n + 1))) == n + 1:
                n += 1
            else:
                fail = True
                break
            i += 1 + int(math.log10(n))

        if not fail:
            return missingNo
    return -1


for _ in range(int(input())):
    s = input()
    missing = []
    if int(s) + 1 <= 99999:
        missing.append(int(s) + 1)
    if int(s) - 1 <= 99999:
        missing.append(int(s) - 1)
    res = findMissingNumber(s)
    if res != -1:
        missing.append(res)

    missing.sort()
    print(len(missing))
    print(*missing)

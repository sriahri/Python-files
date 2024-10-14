def MathChallenge(num):
    res = ''
    c = 0
    num = int(num)
    while num != 0:
        x = num%3
        res = str(x) + res
        num = num//3
    return res


print(MathChallenge(input()))

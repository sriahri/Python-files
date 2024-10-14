def maxStreak(m, data):
    c = 0
    res = 0
    x = 'Y'*m
    for i in data:
        if i == 'x':
            c += 1
        else:
            res = max(c, res)
            c = 0
    return res
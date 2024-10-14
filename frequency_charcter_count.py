def countFrequency(input1):
    from collections import Counter
    d = Counter(input1)
    s = ''
    for i in sorted(d.keys()):
        s += i + str(d[i])
    return s
print(countFrequency('phqgh'))
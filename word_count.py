text = 'How much wood would a woodchuck chuck if a woodchuck could chuck wood'
words = text.split()
d = {}
for i in words:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print('{:>12}{:>10}{:>12}'.format("WORD", "COUNT", "FST_OCCUR"))
for i in d.keys():
    print('{:>12}{:>10}{:>12}'.format(i, d[i], text.index(i)))

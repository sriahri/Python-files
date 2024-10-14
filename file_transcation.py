l = [800]
i = 800
j = 2
n = int(input())
c = 0
while (i + j) < n:
    l.append(i + j)
    i = i + j
    j = j + 2
for i in l:
    s = str(i)
    res = 0
    for j in s:
        res += int(j)
    print(res, end = ' ')
    if res > 9 and res < 20:
        c += 1
print()
print(c)
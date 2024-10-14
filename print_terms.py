n = 100
a = 111
for i in range(1, n-1):
    print(a, end=' ')
    if i % 10 == 0:
        print()
    if a % 2 == 0:
        a = a // 2
    else:
        a = 3 * a + 1

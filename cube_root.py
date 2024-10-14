import math
n = int(input())
l = list(map(int,input().split()))
c = 0
for i in range(n):
    if round(l[i] ** (1/3)) == int(l[i] ** (1/3)):
        print(l[i])
        c += 1
print(c)
print(216 ** (1/3))
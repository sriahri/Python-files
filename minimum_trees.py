
from bisect import bisect
n = int(input())
k = int(input())
l = []
for i in range(n):
    l.append(int(input()))
    
l.sort()
res = 1
if n > 1:
    x = l[1]
if any(l) == 0:
    res = 0
else:
    while k > 0:
        ele = l.pop()
        a = ele - x
        if k >= a and a != 0:
            k -= a
            ele -= a
        else:
            ele -= k
            k = 0
        ins = bisect(l, ele)
        l.insert(ins, ele)
        # print(l)
    for i in l:
        res *= i
print(res)
        
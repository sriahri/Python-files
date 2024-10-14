from collections import Counter
n = int(input())
l=[]
for i in range(n):
    l.append(int(input()))
d = Counter(l)
for i in l:
    if d[i] == 1:
        print(i)
        break
else:
    print(-1)
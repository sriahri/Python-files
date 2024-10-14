res = []
def subarrays(arr):
    for i in range(len(arr) + 1):
        for j in range(i):
            x = (arr[j: i])
            if len(x) > 1:
                res.append(x)
n = int(input())
a = list(map(int, input().split()))
subarrays(a)
s = set()
for i in a:
    s.add(i)
for i in res:
    p = 0
    for j in i:
        p = p|j
    s.add(p)
y = list(s)
print(len(y))
y.sort()
print(*y)
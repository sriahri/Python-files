n = int(input())
l = list(map(int, input().split()))

temp = [0] * (max(l) + 2)
result = [0] * n
res = temp.index(0)
for i in range(n):
    temp[l[i]] = 1
    if res == l[i]:
        res = temp.index(0)
    result[i] = res

print(*result)

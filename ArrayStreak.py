n, k = map(int, input().split())
l = list(map(int,input().split()))  
count = 1
result = []
for i in range(1,n):
    if l[i] - l[i-1] >= k:
        count += 1
    else:
        count = 1
    result.append(count)
print(*result)
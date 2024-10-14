n = int(input())
l = list(map(int, input().split()))
maximum = [0]*n
minimum = [0]*n
maxi = 0
mini = max(l) + 1
for i in range(n):
    mini = min(l[n-i-1], mini)
    minimum[n-i-1] = mini
for i in range(n):
    maxi = max(l[i], maxi)
    maximum[i] = maxi
result = 9999999
print(maximum)
print(minimum)
for i in range(n):
    x = maximum[i] - minimum[i]
    if x < result:
        result = x
print(result)
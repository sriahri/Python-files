n = int(input())
l=[]
for i in range(n):
    l.append(list(map(int,input().split())))
left = 0
right = 0
for i in range(n):
    for j in range(n):
        if i == j:
            left += l[i][j]
        if i+j == n-1:
            right += l[i][j]
print(abs(left - right))
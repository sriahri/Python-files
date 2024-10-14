n = int(input())
even = 1
odd = 2*n
for i in range(1,n+1):
    odd = i * n
    for j in range(1,n+1):
        if i%2 == 0:
            print(odd,end=' ')
            odd -= 1
        else:
            print(even, end=' ')
            even += 1
    even = odd + n + 1
    print()
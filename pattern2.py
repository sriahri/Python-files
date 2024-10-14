n=int(input())
for i in range(n):
    for j in range(n*2+1):
        if j>i and j<n*2+1-i:
            print('\t')
        else:
            print((j),end='')
            
    print()

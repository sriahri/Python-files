n=int(input())
for i in range(n):
    for j in range(n*2+1):
        if j<=i:
            print(chr(j+97),end='')
        elif j>=n*2-i:
            print(chr(j-(n*2-i)+97),end='')
        else:
            print(' ',end='')
    print()
        

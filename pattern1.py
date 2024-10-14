n=int(input())
for i in range(n+1):
    print(' '*(n-i),end='')
    x=i
    for j in range(i*2+1):
        print(x,end='')
        if j>=i:
           x+=1
        else:
            x-=1
    print()

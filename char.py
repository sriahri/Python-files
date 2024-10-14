n=int(input())
p=n*3+2
q=n-2
for i in range(n-1):
    r=(p-q)//2
    print('-'*(r+1),end='')
    x=n-i+1
    for j in range(i*2+1):
        if j>i:
            print(chr(64+x),end='')
            print('-',end='')
            x+=1
        else:
            y=(j)%(i+1)
            print(chr(64+(n-y)),end='')
            print('-',end='')
    print('-'*(r))
    q=q+4
i=n-1
r=(p-q)//2
print('-'*(r+1),end='')
x=n-i+1
for j in range(i*2+1):
    if j>i:
        if j==n*2-2:
            print(chr(64+x),end='')
            x+=1
        else:
            print(chr(64+x),end='')
            print('-',end='')
            x+=1
    else:
        y=(j)%(i+1)
        print(chr(64+(n-y)),end='')
        print('-',end='')
print('-'*(r))
q=q+4
q=n*3
l=[]
for i in range(n-1):
    l.append(i)
for i in l[::-1]:
    r=(p-q)//2
    print('-'*(r+1),end='')
    x=n-i+1
    for j in range(i*2+1):
        if j>i:
            print(chr(64+x),end='')
            print('-',end='')
            x+=1
        else:
            y=(j)%(i+1)
            print(chr(64+(n-y)),end='')
            print('-',end='')
    print('-'*(r))
    q=q-4

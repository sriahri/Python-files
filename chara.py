from math import *
def print_rangoli(size):
    # your code goes here
    p=n*3+2
    q=n+4
    if n%2==0:
        for i in range(n-1):
            r=(p-q)//2
            print('-'*(r+floor(n/2)+(n//2)-1),end='')
            x=n-i+1
            for j in range(i*2+1):
                if j>i:
                    print(chr(96+x),end='')
                    print('-',end='')
                    x+=1
                else:
                    y=(j)%(i+1)
                    print(chr(96+(n-y)),end='')
                    print('-',end='')
            print('-'*(r+floor(n/2)+(n//2)-2))
            q=q+4
    elif n==1:
        print('a')
    else:
         for i in range(n-1):
            r=(p-q)//2
            print('-'*(r+floor(n/2)+(n//2)),end='')
            x=n-i+1
            for j in range(i*2+1):
                if j>i:
                    print(chr(96+x),end='')
                    print('-',end='')
                    x+=1
                else:
                    y=(j)%(i+1)
                    print(chr(96+(n-y)),end='')
                    print('-',end='')
            print('-'*(r+floor(n/2)+(n//2)-1))
            q=q+4
    if n==1:
        pass
    else:
        i=n-1
        r=(p-q)//2
        print('-'*(r+1),end='')
        x=n-i+1
        for j in range(i*2+1):
            if j>i:
                if j==n*2-2:
                    print(chr(96+x),end='')
                    x+=1
                else:
                    print(chr(96+x),end='')
                    print('-',end='')
                    x+=1
            else:
                y=(j)%(i+1)
                print(chr(96+(n-y)),end='')
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
                    print(chr(96+x),end='')
                    print('-',end='')
                    x+=1
                else:
                    y=(j)%(i+1)
                    print(chr(96+(n-y)),end='')
                    print('-',end='')
            print('-'*(r))
            q=q-4
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

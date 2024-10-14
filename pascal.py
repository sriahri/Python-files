from math import *
n=int(input())
for i in range(n):
    print(' '*(n-i),end='')
    for j in range(i+1):
        if j==0:
            print('1',end=' ')
        else:
            print(factorial(i)//(factorial(j)*factorial(i-j)),end=' ')
    print()

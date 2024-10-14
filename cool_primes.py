
from collections import Counter
def isPrime(i):
    if i <= 1:
        return False
    if i <= 3 :
        return True
    if i % 2 == 0 or i % 3 == 0:
        return False
    j = 5
    while j ** 2 <= i:
        if i % j == 0 or i % (j + 2) == 0:
            return False
        j += 1
    return True
l, r = map(int,input().split())
c = 0
if l > 0:
    if l % 2  == 0:
        l += 1
    for i in range(l,r+1,2):
        if isPrime(i):
            #print(i)
            s = str(i)
            #print(d)
            if '2' in s and '3' in s and '5' in s and '7' in s:
                c += 1
print(c,end = ' ')
if isPrime(c):
    print('Yes')
else:
    print('No')
import datetime
import random
print('Name is John Smith')
print()
print('Date is',datetime.date.today())
print()
n = int(input('Enter the value of N : '))
s = int(input('Enter the value of seed : '))
random.seed(s)
l = [random.randint(0,99) for i in range(n)]
print()
print('Before sorting the list : ')
print()
for i in range(n):
    if i%10 != 9:
        print(l[i], end=' ')
    else:
        print(l[i])
l.sort()
print()
print('After Sorting the list : ')
print()
for i in range(n):
    if i%10 != 9:
        print(l[i], end=' ')
    else:
        print(l[i])
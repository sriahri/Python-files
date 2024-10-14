from math import factorial
intput1 = int(input())
input2 = list(map(int, input().split()))

even = []
odd = []
for i in input2:
    if i % 2 == 0:
        even.append(i)
    else:
        odd.append(i)

even_length = len(even)
odd_length = len(odd)
count = 2**even_length - 1
count += (2**even_length - 1) * odd_length

print(count)
for i in range(1, even_length//2):
    count += factorial(even_length)/(factorial(even_length-2*i) * factorial(2*i))

print(count)

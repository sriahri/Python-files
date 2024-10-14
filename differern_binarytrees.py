from math import factorial
n = int(input())
result = (factorial((2*n))/(factorial(n) * factorial(n))/(n+1)) * factorial(n)
print(int(result))
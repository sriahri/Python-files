from math import factorial
for _ in range(int(input())):
    n = int(input())
    if n < 5:
        print(0)
    else:
        if n == 5:
            print(120)
        elif n == 6:
            print(21*factorial(6))
        else:
            print((21*factorial(n) + 21 **(n-7)*factorial(5))%(10**9+7))
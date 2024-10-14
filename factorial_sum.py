from math import factorial
n = 20
fac_sum = 0
for i in range(1, n+1):
    fac = factorial(i)
    print(fac)
    fac_sum += fac
    print(fac_sum)


if fac_sum > 2**63 - 1:
    print('greater')

from fractions import Fraction
n = int(input())
m = int(input())
cities = []
for i in range(n):
    cities.append(int(input()))

cities.sort(reverse=True)
j = 0
if n > m:
    for i in range(m):
        if cities[j] % 2 == 0:
            cities[j] = cities[j]//2
        else:
            cities[j] = cities[j]/2
        j += 1
else:
    x = m//n
    for i in range(n):
        if cities[i] %(2*x) == 0:
            cities[i] = cities[i] // (2*x)
        else:
            cities[i] = cities[i]/(2*x)
    for i in range(m%n):
        if cities[i] % 2 == 0:
            cities[i] = cities[i]//2
        else:
            cities[i] = cities[i]/2
    
a = max(cities)
if isinstance(a, int):
    print(a%(1000000007))
else:
    fr = Fraction(a)
    nume = fr.numerator
    deno = fr.denominator
    res = (nume*(deno**-1))%(1000000007)
    print(res)
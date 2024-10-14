polynomial = '1 3 4 2;4'
result = 0
# The polynomial looks like (x^3 + 3x^2 + 4x + 2)
coefficients = polynomial.split(';')[0]
coefficients = list(map(int, coefficients.split()))
n = int(polynomial.split(';')[1])
degree = len(coefficients) - 1
for i in range(degree, 0, -1):
    result += n**i * coefficients[degree-i]

result += coefficients[-1]
print('The evaluation of expression at n={} is {}'.format(n, result))

m1 = 400 * 20.05
m2 = 400 * 32.03

b1 = (2.2 / 100) * m1
b2 = (2.2 / 100) * m2

profit = m2 - m1 - b1 - b2

print('money that the company paid for the stock:', m1)
print('commission that the company paid the broker on buying the stock: ', round(b1))
print('amount that the company sold the stock for:', m2)
print("commission that the company paid the broker on selling the stock:", round(b2))
print('net profit the company received:', profit)

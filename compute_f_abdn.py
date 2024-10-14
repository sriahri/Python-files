a = (input('Enter the value of a: '))
b0 = (input('Enter the value of b0: '))
n = (input('Enter the value of n: '))
d = (input('Enter the value of d: '))

if a.isnumeric() and b0.isnumeric() and n.isnumeric() and d.isnumeric():
    a = int(a)
    b0 = int(b0)
    n = int(n)
    d = int(d)
    if a < 0 or b0 < 0 or n < 0 or d < 0:
        print('Invalid input! All numbers must be greater than 0')
    else:
        result = 0
        prev_b = b0
        for i in range(1, n+1):
            b = prev_b + 3
            result += (b + i*d) * (a**i)
            prev_b = b

        print('The value of f is', result)
else:
    print('Error')

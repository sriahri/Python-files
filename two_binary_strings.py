def binaryStringSum(num1, num2):
    a = int(num1, 2)
    b = int(num2, 2)

    c = a + b
    s = bin(c)[2:]
    return s
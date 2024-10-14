def sum3Numbers(x, y, z):
    return x + y + z


def multiply3Numbers(x, y, z):
    return x * y * z


def sumUpTo3Numbers(x, y=0, z=0):
    return x + y + z


def multiplyUpTo3Numbers(x, y=1, z=1):
    return x * y * z


def printInOrder(x, y):
    if x > y:
        print(y, x)
    else:
        print(x, y)


def areaOfSquare(side):
    if side < 0:
        print('Negative value entered ')
    else:
        return side * side


def perimeterOfSquare(side):
    if side < 0:
        print('Negative value entered ')
    else:
        return 4 * side


def areaOfCircle(radius):
    if radius < 0:
        print('Negative value entered ')
    else:
        return (22 / 7) * radius * radius


def circumferenceOfCircle(radius):
    if radius < 0:
        print('Negative value entered ')
    else:
        return 2 * (22 / 7) * radius


def bothFactors(d1, d2, x):
    if x % d1 == 0 and x % d2 == 0:
        return True
    return False


def squareAndCircle(x):
    print()
    print('Circle with radius {} has:'.format(x))
    print('Area: {}'.format(areaOfCircle(x)))
    print('Circumference: {}'.format(circumferenceOfCircle(x)))
    print('Square with side {} has:'.format(x))
    print('Area: {}'.format(areaOfSquare(x)))
    print('Perimeter: {}'.format(perimeterOfSquare(x)))
    print()


def factorial(n):
    if n < 0:
        print('Input must be positive')
    elif n < 2:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

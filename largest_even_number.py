def largest_even_number(a, b, c):
    # If a is even and greater than b and c.
    if a%2 == 0 and a >= b and a >= c:
        return a
    # If b is even and greater than a and c.
    elif b%2 == 0 and b >= a and b >= c:
        return b
    # If c is even and greater than a and b.
    elif c % 2 == 0 and c >= a and c >= b :
        return c
    else:
        # We need to return smallest odd number among a, b, c.
        if a <= b and a <= c:
            return a
        elif b <= a and b <= c :
            return b
        else:
            return c

a = int(input('Enter the value of a : '))
b = int(input('Enter the value of b : '))
c = int(input('Enter the value of c : '))
print('The largest value is',largest_even_number(a, b, c))
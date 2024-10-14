from math import sqrt

lower_limit = int(input('Enter the lower limit: '))
upper_limit = int(input('Enter the upper limit: '))

while lower_limit < 0 or upper_limit > 50 or lower_limit > upper_limit:
    print('Please enter lower limit greater than 0 and upper limit less than 50')
    print('Make sure the upper limit is always greater than the lower limit')
    lower_limit = int(input('Enter the lower limit: '))
    upper_limit = int(input('Enter the upper limit: '))

print(f"{'Number' : <10}{'SquareRoot' : ^5}{'Square' : ^10}{'Cube' : >5}")
for i in range(lower_limit, upper_limit + 1):
    square_root = round(sqrt(i), 3)
    print(f"{i : <10}{square_root : ^10}{i**2 : ^10}{i**3 : >5}")

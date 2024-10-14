print('***Welcome to Geometry Calculator***')
choice = int(input('Enter your choice: '))
if choice >= 10:
    X = float(input('Enter X: '))
    area = 1/2 * X * (X/2)
    print('Using input {} Area of Triangle {}'.format(X, area))

else:
    X = float(input('Enter X: '))
    area = X * X
    print('Using input {} Area of Square {}'.format(X, area))

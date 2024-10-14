from math import factorial,sin
angle = float(input('Enter the angle in radians: '))
taylor_series = angle - (angle**3)/factorial(3) + (angle**5)/factorial(5) - (angle**7)/factorial(7)
actual_value = sin(angle)
print('Using Taylor Series Approximation, sin(',angle,') = ',taylor_series)
print('Using Math Function, sin(',angle,') = ',actual_value)
print('Approximation Error = %.6f'%abs(actual_value - taylor_series))
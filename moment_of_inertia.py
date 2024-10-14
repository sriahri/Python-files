M = float(input("Enter the mass: "))
R = float(input("Enter the radius: "))

if M < 0 or R < 0:
    print('Inputs must be positive values')
else:
    I = 0.5 * M * R * R
    print('Moment of Inertia is {}'.format(I))

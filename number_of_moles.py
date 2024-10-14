pressure = float(input('Enter the pressure: '))
length = float(input('Enter the length: '))
breadth = float(input('Enter the breadth: '))
height = float(input('Enter the height: '))
temperature = float(input('Enter the temperature: '))
temperature = temperature + 273.14
R = 8.314
volume = length * breadth * height
number_of_moles = (pressure * volume)/(R*temperature)

print('The number of moles is {}'.format(number_of_moles))
rounded_value = round(number_of_moles)
print('The rounded value for the number of moles is {}'.format(rounded_value))
if rounded_value % 2 == 0:
    rounded_value += 1
else:
    rounded_value += 1

print('The rounded even/odd value is {}'.format(rounded_value))

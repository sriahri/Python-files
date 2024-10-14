number = int(input('Enter a number between 1 and 5(included): '))

while not 1 <= number <= 5:
    print('Please enter a valid number between 1 and 5')
    number = int(input('Enter a number between 1 and 5(included): '))


item = None
if number == 1:
    item = 'Pizza'
elif item == 2:
    item = 'Hamburger'
elif item == 3:
    item = 'Fries'
elif item == 4:
    item = 'Soft drink'
else:
    item = 'Milk shake'

print('The item ordered is', item)

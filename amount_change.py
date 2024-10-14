available_dollars = int(input("Enter the available dollars : "))
available_quarters = int(input("Enter the available quarters : "))
available_dimes = int(input("Enter the available dimes : "))
available_nickels = int(input("Enter the available nickels : "))
available_pennies = int(input("Enter the available pennies : "))

money = [available_dollars, available_quarters, available_dimes, available_nickels, available_pennies]

price = float(input('Enter the price: '))
amount_paid = float(input('Enter the amount paid: '))
change = amount_paid - price

print('The change is $', change)
change = change * 100
num_dollars = change // 100
change = change % 100
num_quarters = change // 25
change = change % 25
num_dimes = change // 10
change = change % 10
num_nickels = change // 5
change = change % 5
num_pennies = change

if num_dollars != 0:
    print('{} dollars'.format(int(num_dollars)))
    money[0] -= num_dollars
if num_quarters != 0:
    print('{} quarters '.format(int(num_quarters)))
    money[1] -= num_quarters
if num_dimes != 0:
    print('{} dimes'.format(int(num_dimes)))
    money[2] -= num_dimes
if num_nickels != 0:
    print('{} nickels'.format(int(num_nickels)))
    money[3] -= num_nickels
if num_pennies != 0:
    print('{} pennies'.format(int(num_pennies)))
    money[4] -= num_pennies

def minCoins(money, dimes, quarters, pennies):
    # Because 25 cents is equal to 1 quarter
    no_of_quarters = money//25
    if quarters < no_of_quarters :
        no_of_quarters = quarters
    money = money - no_of_quarters * 25
    # 1 dime = 10 cents
    no_of_dimes = money//10
    if dimes < no_of_dimes :
        no_of_dimes = dimes
    money = money - no_of_dimes * 10
    no_of_pennies = money
    if no_of_pennies > pennies :
        return 'Reimbursing is not possible.'
    return no_of_quarters + no_of_dimes + no_of_pennies 

balance = float(input("Enter the balance amount : "))
available_quarters = int(input("Enter the available quarters : "))
available_dimes = int(input("Enter the available dimes : "))
available_pennies = int(input("Enter the available pennies : "))
print(minCoins(balance, available_dimes, available_quarters, available_pennies))
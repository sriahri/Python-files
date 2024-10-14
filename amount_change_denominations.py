def coinCalc(change):
    num_quarters = change // 25
    change = change % 25
    num_dimes = change // 10
    change = change % 10
    num_nickels = change // 5
    change = change % 5
    num_pennies = change

    return num_quarters, num_dimes, num_nickels, num_pennies


def main():
    print("Coin Return Calculator")
    flag = 1
    while flag == 1:
        try:
            amount = int(input('\nEnter the change amount to convert: '))
            # Calling the function
            quarters, dimes, nickels, pennies = coinCalc(amount)
            if quarters > 0:
                print('{} quarter(s)'.format(quarters))
            if dimes > 0:
                print('{} dime(s)'.format(dimes))
            if nickels > 0:
                print('{} nickel(s)'.format(nickels))
            if pennies > 0:
                print('{} penny(ies)'.format(pennies))
        except:
            print(' Error! Invalid integer entered please try again.')
            continue
        # Asking the user whether to continue
        choice = input('\nWant to calculate another amount? (y/n): ')
        if choice == 'y':
            flag = 1
        else:
            flag = 0
        print('\nBye!')


if __name__ == '__main__':
    main()

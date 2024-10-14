pin = int(input("Enter the pin number: "))
stored_pin = 1234
account_balance = 21000
if pin == stored_pin:
    while True:
        print('For with drawl press 1\nFor view balance press 2\nTo Exit Press 3')
        choice = int(input("Enter your choice: "))
        if choice == 1:
            amount = float(input("Enter the amount to with drawl: "))
            if amount > account_balance:
                print("Not possible! Please check the balance")
            else:
                account_balance -= amount
                print('Your current balance is {}'.format(account_balance))
        elif choice == 2:
            print('Your current balance is {}'.format(account_balance))
        elif choice == 3:
            break
        else:
            print('Wrong Option!')
else:
    print('Wrong Pin! Try again')

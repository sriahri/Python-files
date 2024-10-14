
while 1 :
    name = input("Enter name: ")
    address = input("Enter address: ")
    amount = input("Enter amount of purchase: ")[1:]
    type = input("Enter the type of purchase (L for Laptop and D for Desktop): ")
    net_amount = 0
    print()
    amount = int(amount)
    if type == 'L':
        if amount > 0 and amount <= 250 :
            net_amount = amount
        elif amount > 250  and amount <= 570 :
            net_amount = amount - amount * 0.05
        elif amount > 570  and amount <= 1000 :
            net_amount = amount - amount * 0.075
        else:
            net_amount = amount - amount * 0.1
    elif type == 'D':
        if amount > 0 and amount <= 250 :
            net_amount = amount - amount * 0.05
        elif amount > 250  and amount <= 570 :
            net_amount = amount - amount * 0.076
        elif amount > 570  and amount <= 1000 :
            net_amount = amount - amount * 0.1
        else:
            net_amount = amount - amount * 0.15
    else:
        print('Inavlid type of purchase')
        print()
    if type == 'L' or type == 'D':
        print('Name:',name)
        print('Address:',address)
        print('Net amount: $%.2f'%net_amount)
        print()
    choice = input('Do you wish to continue purchase: ')
    print()
    if choice == 'Y':
        pass
    else:
        print()
        print('You have exit purchase screen, Goodbye')
        break
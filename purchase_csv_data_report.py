def get_report(filename):
    file = open(filename)
    lines = file.readlines()

    purchases = {}
    for line in lines:
        category, cost = map(str, line.split(','))
        if category in purchases:
            purchases[category].append(int(cost.strip()))
        else:
            purchases[category] = list([int(cost.strip())])

    total_cost = 0
    for category, cost in purchases.items():
        for each_cost in cost:
            total_cost += each_cost

    print('Total Cost is:', total_cost)

    total_purchases = 0
    for category, cost in purchases.items():
        total_purchases += len(cost)

    print('Number of Purchases:', total_purchases)

    print('Average purchase cost:', total_cost/total_purchases)
    for category, cost in purchases.items():
        print('Category: {}, Number of Purchases: {}'.format(category, len(cost)))

    for category, cost in purchases.items():
        print('Category: {}, Purchases: {}'.format(category, cost))

    minimum_purchase = 99999999999999
    for category, cost in purchases.items():
        if min(cost) < minimum_purchase:
            minimum_purchase = min(cost)

    for category, cost in purchases.items():
        if minimum_purchase in cost:
            print('Category: {}, Minimum Purchase: {}'.format(category, minimum_purchase))

    maximum_purchase = 0
    for category, cost in purchases.items():
        if max(cost) > maximum_purchase:
            maximum_purchase = max(cost)

    for category, cost in purchases.items():
        if maximum_purchase in cost:
            print('Category: {}, Maximum Purchase: {}'.format(category, maximum_purchase))


if __name__ == '__main__':
    choice = 'yes'
    while choice.lower() == 'yes':
        filename = input('Enter the filename: ')
        get_report(filename)
        choice = input('Do you want to continue: [yes/no]: ')
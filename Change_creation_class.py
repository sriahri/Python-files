class Change:
    def __init__(self, coins2, bills5, bills10):
        self.coins2 = coins2 if coins2 else 0
        self.bills5 = bills5 if bills5 else 0
        self.bills10 = bills10 if bills10 else 0

    def __str__(self):
        return 'Coins2: {}\nBills5: {}\nBills10: {}\n'.format(self.coins2, self.bills5, self.bills10)


def getChange(amount):
    bills10 = amount // 10
    amount = amount % 10
    if amount % 2 == 0 and (amount % 5) % 2 != 0:
        coins2 = amount // 2
        amount = amount % 2
        bills5 = 0
    else:
        bills5 = amount // 5
        amount = amount % 5
        coins2 = amount // 2
        amount = amount % 2
    if amount != 0:
        return None
    return Change(coins2, bills5, bills10)


if __name__ == '__main__':
    print()
    change = getChange(1)
    print(change)

    print()
    change = getChange(6)
    print(change)

    print()
    change = getChange(10)
    print(change)

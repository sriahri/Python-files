# We know that the cents that are available are 1, 5, 10, 25, 50.
def get_change(amount):
    number_of_50_cents = amount // 50
    amount = amount % 50
    number_of_25_cents = amount // 25
    amount = amount % 25
    number_of_10_cents = amount // 10
    amount = amount % 10
    number_of_5_cents = amount // 5
    amount = amount % 5
    number_of_1_cents = amount

    print('The number of 50 cents coins are {}'.format(number_of_50_cents))
    print('The number of 25 cents coins are {}'.format(number_of_25_cents))
    print('The number of 10 cents coins are {}'.format(number_of_10_cents))
    print('The number of 5 cents coins are {}'.format(number_of_5_cents))
    print('The number of 1 cents coins are {}'.format(number_of_1_cents))


if __name__ == '__main__':
    amount_to_change = 97
    get_change(amount_to_change)

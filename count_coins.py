def next_largest_coin(coin):
    if coin == 1:
        return 5
    elif coin == 5:
        return 10
    elif coin == 10:
        return 25


def count_coins(total):
    coins_list = [1]
    coins_list.append(next_largest_coin(coins_list[-1]))
    coins_list.append(next_largest_coin(coins_list[-1]))
    coins_list.append(next_largest_coin(coins_list[-1]))
    n = len(coins_list)

    change = [0 for i in range(total + 1)]
    change[0] = 1
    for i in range(n):
        for j in range(coins_list[i], total + 1):
            change[j] += change[j - coins_list[i]]

    return change[total]


total = int(input("Enter the amount: "))
print('The number of ways are {}'.format(count_coins(total)))

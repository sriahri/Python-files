def maxProfit(price):
    n = len(price)
    if n == 0:
        return -1
    if n < 2:
        return 0
    buy1, buy2 = 999999999, 99999999
    profit1, profit2 = 0, 0
    for i in range(n):
        buy1 = min(buy1, price[i])
        profit1 = max(profit1, price[i] - buy1)
        buy2 = min(buy2, price[i] - profit1)
        profit2 = max(profit2, price[i] - buy2)
    return profit2
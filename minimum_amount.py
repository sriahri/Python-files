def minimumAmount(prices):
    ans = [prices[0]]
    mini = prices[0]
    for i in range(1, len(prices)):
        mini = min(mini, prices[i])
        ans.append(prices[i]-mini)
    return sum(ans)
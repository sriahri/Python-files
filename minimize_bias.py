def minimizeBias(ratings):
    ratings.sort()
    bias_amount = 0
    n = len(ratings)
    for i in range(0,n-1,2):
        bias_amount += ratings[i+1] - ratings[i]
    return bias_amount

ratings = list(map(int,input().split()))
print(minimizeBias(ratings))
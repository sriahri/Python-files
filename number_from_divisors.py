def solve(X, D):
    count = 0
    for i in range(1, X*(10**D) + 1):
        a = X/i
        a = str(a).split('.')[1]
        re = len(a) if a != '0' else 0
        if re <= D:
            count += 1
    return count


# print(solve(7, 1))
print(solve(6, 0))

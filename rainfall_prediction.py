def predictDays(days, k):
    n = len(days)
    res = []
    for i in range(k, n - k):
        for j in range(k, 0, -1):
            if days[j + i] < days[j + i - 1]:
                break
        else:
            res.append(i + 1)
        for j in range(k):
            if days[j + i] > days[j + i + 1]:
                break
        else:
            if (i + 1) not in res:
                res.remove(i+1)

    return sorted(res)


if __name__ == '__main__':
    print(predictDays([3, 2, 2, 2, 3, 4], 2))
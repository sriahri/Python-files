def getHeaviestPackage(weights):
    copy_weights = weights.copy()
    n = len(weights)
    copy_weights[n-1] = weights[n-1]
    for i in range(n-2, -1, -1):
        if weights[i] < copy_weights[i+1]:
            copy_weights[i] = copy_weights[i+1] + weights[i]
        else:
            copy_weights[i] = weights[i]
    return max(copy_weights)


if __name__ == '__main__':
    weights = [2, 9, 10, 3, 7]
    print(weights)
    print('The heaviest weight possible is ', end=' ')
    print(getHeaviestPackage(weights))

    weights = [20, 13, 8, 9]
    print(weights)
    print('The heaviest weight possible is ', end=' ')
    print(getHeaviestPackage(weights))

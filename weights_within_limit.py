if __name__ == '__main__':
    weights = list(map(float, input('Enter the weights: ').split()))
    max_weight = float(input('Enter the weight of bag: '))

    weights.sort()
    total_weight = 0
    res = []
    for i in weights:
        total_weight += i
        if total_weight < max_weight:
            res.append(i)
        else:
            break

    print(res)

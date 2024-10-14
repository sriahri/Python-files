if __name__ == '__main__':
    values = [12, 1, 10, 8]
    weights = [4, 1, 5, 2]
    max_weight = 10
    length = len(values)  # number of items

    # Table for dynamic programming
    table = [[0 for _ in range(max_weight + 1)] for __ in range(length + 1)]

    # Build table in bottom up manner
    for i in range(length + 1):
        for weight in range(max_weight + 1):
            if i == 0 or weight == 0:
                table[i][weight] = 0
            #  The formula is if weights[i-1] <= weight then
            # table[i][weight] = maximum(values[i - 1] + table[i - 1][weight - weights[i - 1]], table[i - 1][weight])
            # if not then, table[i][weight] = table[i - 1][weight]
            elif weights[i - 1] <= weight:
                table[i][weight] = max(values[i - 1]
                                       + table[i - 1][weight - weights[i - 1]],
                                       table[i - 1][weight])
            else:
                table[i][weight] = table[i - 1][weight]

    for i in table:
        print(i)



import numpy as np


def q5_func(data, first_day):
    data = list(data[(7 - first_day + 1) % 7:])
    n = len(data)
    count = 0
    for i in range(n % 7):
        data.pop()
    i = 0
    while i < len(data) - 6:
        x = data[i:i + 5]
        a = x.copy()
        x.sort()
        if x == a:
            count += 1
        i += 7
    return count


data = np.array([23, 26, 21, 23, 25, 26, 24, 26, 22, 21, 23, 23, 25, 26, 24, 23, 22, 23, 24, 26, 28, 27, 30, 29, 29, 27])
first_day = 6
print('The number of weeks are {}'.format(q5_func(data, first_day)))

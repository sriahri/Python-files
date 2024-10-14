import numpy as np


if __name__ == '__main__':
    array1 = np.array([[12, 3, 5], [21, 8, 10], [10, 19, 43]])
    array2 = np.array([[2, 13, 6], [19, 18, 9], [11, 9, 3]])

    print('Adding 2 arrays:')
    result = array1 + array2
    print(result)

    print('Subtracting 2 arrays:')
    result = array1 - array2
    print(result)

    print('Multiplying 2 arrays:')
    result = array1 * array2
    print(result)

    print('Dividing 2 arrays:')
    result = array1 / array2
    print(result)

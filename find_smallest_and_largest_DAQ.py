import sys


def find_min_and_max(array, low, high, smallest=sys.maxsize, largest=-sys.maxsize):
    if low == high:
        if smallest > array[high]:
            smallest = array[high]

        if largest < array[low]:
            largest = array[low]

        return smallest, largest

    elif abs(low - high) == 1:
        if array[low] < array[high]:
            if smallest > array[low]:
                smallest = array[low]

            if largest < array[high]:
                largest = array[high]

        else:
            if smallest > array[high]:
                smallest = array[high]

            if largest < array[low]:
                largest = array[low]

        return smallest, largest

    mid = (low + high) // 2
    smallest, largest = find_min_and_max(array, low, mid, smallest, largest)
    smallest, largest = find_min_and_max(array, mid + 1, high, smallest, largest)

    return smallest, largest


if __name__ == '__main__':
    small, large = find_min_and_max([1, 7, 89, 87, 65, 46], 0, 5)
    print('The smallest element is {} and the largest element is {}'.format(small, large))

def find_min_and_max(array):
    array.sort()
    smallest = array[0]
    largest = array[-1]
    print('The smallest element is {} and the largest element is {}'.format(smallest, largest))


if __name__ == '__main__':
    find_min_and_max([1, 7, 89, 87, 65, 46])

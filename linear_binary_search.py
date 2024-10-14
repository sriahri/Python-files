def linear_search(numbers, key):
    count = 1
    for i in range(len(numbers)):
        if numbers[i] == key:
            return i, count
        count += 1
    return -1, -1


def binary_search(numbers, key):
    length = len(numbers)
    first = 0
    last = length - 1
    mid = 0
    count = 0
    while first <= last:
        count += 1
        mid = (last + first) // 2
        if numbers[mid] < key:
            first = mid + 1
        elif numbers[mid] > key:
            last = mid - 1
        else:
            return mid, count
    return -1, -1


if __name__ == '__main__':
    while True:
        print('''1. Linear search
2. Binary Search
3. Exit''')

        numbers = []
        choice = int(input('Enter your choice: '))
        if choice == 1:
            numbers = list(map(int, input('Enter 10 numbers in any order: ').split()))
            element = int(input('Enter the key you want to search: '))
            index, operations = linear_search(numbers, element)
            if index == -1:
                print('Search is not successful')
            else:
                print("Search successful and the position is :", index)
                print("The number of steps to find the numbers is: ", operations)

        elif choice == 2:
            numbers = list(map(int, input('Enter 10 numbers in sorted order: ').split()))
            element = int(input('Enter the key you want to search: '))
            index, operations = binary_search(numbers, element)
            if index == -1:
                print('Search is not successful')
            else:
                print("Search successful and the position is :", index)
                print("The number of steps to find the numbers is: ", operations)
        else:
            break

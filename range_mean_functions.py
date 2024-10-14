def range_of_list_firstname(number_list):
    return max(number_list) - min(number_list)


def mean_of_list_firstname(number_list):
    return sum(number_list) / len(number_list)


def median_of_list_firstname(number_list_copy):
    number_list_copy.sort()
    n = len(number_list_copy)
    if n % 2 == 0:
        return (number_list_copy[n // 2] + number_list_copy[n // 2 + 1]) / 2
    else:
        return number_list_copy[n // 2]


def intersection_lists(number_list, number_list2):
    res = []
    for i in number_list:
        if i in number_list2:
            res.append(i)
    return res


def union_lists(number_list, number_list2):
    res = number_list.copy()
    for i in number_list2:
        if i not in number_list:
            res.append(i)
    return res


def main():
    n = int(input('Enter the number of elements: '))
    number_list = []
    for i in range(n):
        number_list.append(int(input("Enter the number {}: ".format(i + 1))))

    print("Given List:", number_list)
    print('Range of the List is:', range_of_list_firstname(number_list))
    print('Mean of the List is:', mean_of_list_firstname(number_list))
    print('Median of the List is:', median_of_list_firstname(number_list.copy()))

    number_list2 = []
    length = n
    import random
    for i in range(length):
        number_list2.append(random.randint(10, 99))

    print('Second List created using random numbers:', number_list2)
    print('Intersection of the list:', intersection_lists(number_list, number_list2))
    print('Union of the list:', union_lists(number_list, number_list2))


if __name__ == '__main__':
    main()

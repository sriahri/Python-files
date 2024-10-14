# Function that returns a value
def return_sum_of_list(elements, length):
    print('Inside the function that returns the value')
    sum_of_elements = 0
    for i in range(length):
        sum_of_elements += elements[i]
    return sum_of_elements


# Function that does not return a value
def print_sum_of_list(elements, length):
    print('Inside the function that does not return')
    sum_of_elements = 0
    for i in range(length):
        sum_of_elements += elements[i]
    print('Sum of elements in the list is {}'.format(sum_of_elements))


if __name__ == '__main__':
    elements_list = [2.3, 4, 5.6, 7, 8, 19]
    # Calling the function that returns the value
    n = len(elements_list)
    result = return_sum_of_list(elements_list, n)
    print('The result is {}'.format(result))

    # Calling the function that does not return the value
    print_sum_of_list(elements_list, n)

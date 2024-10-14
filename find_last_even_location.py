def find_last_even_integer(numbers):
    result = 0
    for i in range(len(numbers)-1, -1, -1):
        if numbers[i] % 2 == 0:
            result = i + 1
            break
    return result


if __name__ == '__main__':
    numbers = [12, 23, 24, 35, 27, 68, 70, 79]
    print(find_last_even_integer(numbers))
    numbers = [11, 23, 89, 35, 27, 69, 77, 79]
    print(find_last_even_integer(numbers))

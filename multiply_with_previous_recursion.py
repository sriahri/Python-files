def calculate_nth(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        return calculate_nth(n-2) * calculate_nth(n-1)


if __name__ == '__main__':
    n_number = 3
    print('The {}th number in the series is {}'.format(n_number, calculate_nth(n_number)))
    n_number = 4
    print('The {}th number in the series is {}'.format(n_number, calculate_nth(n_number)))
    n_number = 5
    print('The {}th number in the series is {}'.format(n_number, calculate_nth(n_number)))
    n_number = 6
    print('The {}th number in the series is {}'.format(n_number, calculate_nth(n_number)))
    n_number = 7
    print('The {}th number in the series is {}'.format(n_number, calculate_nth(n_number)))
    n_number = 8
    print('The {}th number in the series is {}'.format(n_number, calculate_nth(n_number)))
    n_number = 9
    print('The {}th number in the series is {}'.format(n_number, calculate_nth(n_number)))
    n_number = 10
    print('The {}th number in the series is {}'.format(n_number, calculate_nth(n_number)))

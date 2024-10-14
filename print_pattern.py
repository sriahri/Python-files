def print_inverted_triangle_pattern(n):
    for i in range(1, n + 1):
        for j in range(i - 1, n):
            print(i, end='')
        print(' ' * (2 * (i - 1)), end='')
        for j in range(i - 1, n):
            print(i, end='')
        print()


if __name__ == '__main__':
    n = int(input('Enter the value of n: '))
    print_inverted_triangle_pattern(n)

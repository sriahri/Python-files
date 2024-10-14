if __name__ == '__main__':
    n = int(input())
    count = 1
    while n <= 0:
        print('Please enter positive integer')
        n = int(input())

    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        count += 1
    print('Number of terms: {}'.format(count))

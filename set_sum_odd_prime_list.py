def set_sum(A, B):
    res = []
    for i in B:
        for j in A:
            if (i + j) not in res:
                res.append(i + j)
    return res


def is_prime(n):
    from math import sqrt
    for i in range(2, int(sqrt(n))):
        if n % i == 0:
            return False
    return True


def odd_prime_list(n):
    res = []
    for i in range(3, n + 1, 2):
        if is_prime(i):
            res.append(i)
    return res


if __name__ == '__main__':
    A = [1, 2, 3]
    B = [5, 10]
    result = set_sum(A, B)
    print('Result of sum_set: ', result)

    n = 20
    result = odd_prime_list(n)
    print('Odd prime list till {} is {}'.format(n, result))

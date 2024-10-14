def maximum(l):
    n = len(l)
    if n == 0:
        return None
    elif n == 1:
        return l[0]
    elif n == 2:
        return l[0] if l[0] > l[1] else l[1]
    return max(maximum(l[:n // 2]), maximum(l[n // 2:]))


def max(n1, n2):
    return n1 if n1 > n2 else n2


if __name__ == '__main__':
    l = [10, 20, 30]
    print(maximum(l))
    l = [21, 32, 43, 54, 12, 6, 33]
    print(maximum(l))

def minimumPrime(n):
    i = 2
    x = 1
    while i * i < n:
        if n%i == 0:
            x = i
            break
        i += 1
    return n - x
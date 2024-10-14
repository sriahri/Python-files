def findAutoCount(n):
    zeroes = int(n[0])
    ones = int(n[1])
    x = n.count('0')
    y = n.count('1')
    if (x == zeroes and y == ones):
        s = set(n)
        return len(list(s))
    return 0
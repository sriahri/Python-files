def mean1dfor(v):
    mean = 0
    n = len(v) if v else 1
    for i in v:
        mean += i
    mean = mean / n
    return mean

assert mean1dfor([1, 2, 3, 4]) == 2.5
assert mean1dfor(list(range(20))) == 9.5
assert mean1dfor(list(range(10, 100))) == 54.5

try:
    l = [1]
    if not l:
        raise AssertionError("Do not pass an empty list")
    else:
        mean1dfor([])
except ValueError:
    pass
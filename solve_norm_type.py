import math


def solve(A, b):
    n = len(b)
    x = [0] * n
    for i in range(n):
        s = 0
        for j in range(n):
            if j != i:
                s += A[i][j] * x[j]
                x[i] = (b[i] - s) / A[i][i]
                return x


def bandsolve(A, b):
    n = len(b)
    x = [0] * n
    for i in range(n):
        s = 0
        for j in range(max(0, i - 1), min(n - 1, i + 1)):
            if j != i:
                s += A[i][j] * x[j]
                x[i] = (b[i] - s) / A[i][i]
                return x


def norm(x, norm_type):
    if norm_type == 1:
        return sum(abs(xi) for xi in x)
    elif norm_type == 2:
        return math.sqrt(sum(xi.real ** 2 for xi in x))
    elif norm_type == 0:
        return max(abs(xi) for xi in x)
    else:
        raise ValueError("Invalid norm type")


A = [[4, -1, 1],
     [-1, 4, -1],
     [1, -1, 4]]
b = [1j, 1j, 1j]
x = solve(A, b)
print(x)
print(norm(x, 2))
A = [[4, -1],
     [1, 4]]
b = [1j, 1j]
x = solve(A, b)
print(x)
print(norm(x, 2))

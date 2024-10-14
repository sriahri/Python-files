def g(L, v, s=1):
    i = 0
    j = len(L)
    while j != i:
        if s * (L[(j - i) // 2] - v) < 0:
            i = i + (j - i) // 2 + 1
        else:
            j = j - (j - i) // 2 - 1
    return L[: i] + [v] + L[i:]


def f(L):
    if not L:
        return ([], 0, 0)
    else:
        M = f(L[1:])
        if L[0] % 2 == 0:
            return g(M[0][: M[1]], L[0]) + M[0][M[2]:], M[1], M[2]  # Missing code A
        else:
            return M[0][: M[1]] + g(M[0][M[2]:], L[0], -1), M[1] + 1, M[2] + 1


def sort(L):
    return f(L)[0]


print(sort([1, 2, 3, 4, 5, 6, 7, 8, 9]))

def search(L, n, x):
    i = 0
    j = 0
    while i < n:
        if L[j] == x:
            return j
        else:
            j = j+2
        if j >= n-1:
            j = 1
        i = i + 1
    return -1

print(search([1, 4, 5], 3, 5))
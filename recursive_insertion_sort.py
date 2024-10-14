def insertionSort(A,n):
    if n <= 1:
        return
    insertionSort(A, n - 1)
    key  = A[n-1]
    i = n - 2;
    while i >= 0 and A[i] > key:
        A[i+1] = A[i]
        i = i - 1
    A[i+1] = key

array = [40, 23, 56, 12, 76]
n = len(array)
insertionSort(array, n)
print(*array)
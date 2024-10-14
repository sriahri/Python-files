def heapify(arr, n, i):
    left = 2*i + 1
    right = 2*i + 2
    largest = i
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr, n):
    for i in range(n//2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, -1, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def merge(arr, L, R):
    i, j, k = 0, 0, 0
    while L and i < len(L) and R and j < len(R):
        if L[i] > R[j]:
            arr[k] = R[j]
            j += 1
        else:
            arr[k] = L[i]
            i += 1
        k += 1
    while L and i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1
    while R and j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1
    return arr

def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]
        L = mergesort(L)
        R = mergesort(R)
        merge(arr, L, R)
    return arr

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quicksort(arr, low, high):
    if len(arr) <= 1:
        return
    if low < high:
        p = partition(arr, low, high)
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        minindex = i
        for j in range(i + 1, n):
            if arr[minindex] > arr[j]:
                minindex = j
        arr[minindex], arr[i] = arr[i], arr[minindex]


def bubblesort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i- 1):
            if arr[j] > arr[j + 1]:
                arr[j + 1], arr[j] = arr[j], arr[j + 1]


arr = [98, 78, 67, 198, 143, 123, 11, 77, 9, 100, -1, -986]
# heapsort(arr, 10)
# print(arr)
mergesort(arr)
print(arr)

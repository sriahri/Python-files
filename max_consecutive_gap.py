def printResult(arr, arr_size):

    max_gap = 0
    for i in range(1, arr_size):
        if abs(arr[i] - arr[i-1]) > max_gap:
            max_gap = abs(arr[i] - arr[i-1])
    print(max_gap)


def main():
    strs = input()
    strs = strs.split()
    arr = []
    for s in strs:
        arr.append(int(s))
    printResult(arr, len(arr))


main()

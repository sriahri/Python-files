def fun(arr):
    arr.sort()
    return sum(arr[::2]) - sum(arr[1::2])

n = int(input())
l = list(map(int, input().split()))
print(fun(l))
if __name__ == '__main__':
    arr = list(map(int, input().split()))
    d = int(input())
    sub_lists = [[]]
    for i in range(len(arr) + 1):
        for j in range(i):
            sub_lists.append(arr[j: i])

    sub_lists.sort(key=lambda x: len(x))
    total_sum = sum(arr)

    if total_sum % d == 0:
        print(0)
    else:
        for i in sub_lists[1:]:
            if (total_sum - sum(i)) % d == 0 and len(i) != len(arr):
                print(i)
                break

        else:
            print(-1)

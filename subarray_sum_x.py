def sub_array(array, sum):
    # Sum is the value that we need to find
    hashmap = {}
    n = len(array)
    current_sum = 0
    for i in range(0, n):
        current_sum += array[i]
        if current_sum == sum:
            return 0, i
        if current_sum - sum in hashmap:
            return hashmap[current_sum - sum] + 1, i

        hashmap[current_sum] = i

    return None


if __name__ == '__main__':
    arr = [12, 26, 11, 39, 41, 32]
    sum = 33
    res = sub_array(arr, sum)
    if res is None:
        print('No sub array is found')
    else:
        print('The sum {} is present from {} to {}'.format(sum, res[0], res[1]))
    sum = 50
    res = sub_array(arr, sum)
    if res is None:
        print('No sub array is found')
    else:
        print('The sum {} is present from {} to {}'.format(sum, res[0], res[1]))

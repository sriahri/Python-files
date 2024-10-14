def permutation(input, left, right):
    if left == right:
        print(''.join(input))

    else:
        for i in range(left, right):
            input[left], input[i] = input[i], input[left]
            permutation(input, left + 1, right)
            input[left], input[i] = input[i], input[left]


if __name__ == '__main__':
    permutation(['a', 'b', 'c'], 0, 3)

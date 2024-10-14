def find_longest_palindromic_subsequence(input_string, reversed_string, m, n, result):
    if m == 0 or n == 0:
        return ""
    if input_string[m - 1] == reversed_string[n - 1]:
        return find_longest_palindromic_subsequence(input_string, reversed_string, m - 1, n - 1, result) + input_string[m - 1]

    if result[m - 1][n] > result[m][n - 1]:
        return find_longest_palindromic_subsequence(input_string, reversed_string, m - 1, n, result)
    return find_longest_palindromic_subsequence(input_string, reversed_string, m, n - 1, result)


def find_lps_length(input_string, reversed_string, n, result):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if input_string[i - 1] == reversed_string[j - 1]:
                result[i][j] = result[i - 1][j - 1] + 1
            else:
                result[i][j] = max(result[i - 1][j], result[i][j - 1])

    return result[n][n]


def main():
    input_string = input('Enter the string: ')
    reversed_string = input_string[::-1]
    length = len(input_string)
    result = [[0 for X in range(length + 1)] for Y in range(length + 1)]
    find_lps_length(input_string, reversed_string, length, result)
    print('The longest palindromic subsequence is',
          find_longest_palindromic_subsequence(input_string, reversed_string, length, length, result))


if __name__ == '__main__':
    main()

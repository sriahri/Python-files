T = int(input())
x = 0
for t in range(T):
    test_cases = []
    n, k = map(int, input().split())
    inflate = list(map(int, input().split()))
    deflate = list(map(int, input().split()))
    for de in range(n):
        test_cases.append(inflate[de] - deflate[de])

    dp = [[False] * (k + 1) for _ in range(n + 1)]
    dp[0][x] = True

    for i in range(1, n + 1):
        for j in range(k + 1):
            if dp[i - 1][j]:
                if j + test_cases[i - 1] <= k:
                    dp[i][j + test_cases[i - 1]] = True
                if j - test_cases[i - 1] >= 0:
                    dp[i][j - test_cases[i - 1]] = True

    result = []
    curr_value = -1
    for j in range(k, -1, -1):
        if dp[n][j]:
            curr_value = j
            break

    if curr_value == -1:
        print(-1)
        continue

    for i in range(n, 0, -1):
        if curr_value + test_cases[i - 1] <= k and dp[i - 1][curr_value + test_cases[i - 1]]:
            result.append(i - 1)
            curr_value += test_cases[i - 1]
        elif curr_value - test_cases[i - 1] >= 0 and dp[i - 1][curr_value - test_cases[i - 1]]:
            result.append(i - 1)
            curr_value -= test_cases[i - 1]

    print('#'+ str(t), x + sum(result[::-1]))

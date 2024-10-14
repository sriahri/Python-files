def findMinTime(n, cache):
    m = len(cache)
    cache.sort(reverse=True)

    def dfs(i):
        if i == m:
            return True
        for j in range(n):
            if cap[j] >= cache[i]:
                cap[j] -= cache[i]
                if dfs(i + 1):
                    return True
                cap[j] += cache[i]
            if cap[j] == x:
                break
        return False

    # binary search
    left, right = max(cache), sum(cache)
    while left < right:
        x = (left + right) / 2
        cap = [x] * n
        if dfs(0):
            right = x
        else:
            left = x + 1
    return left

if __name__ == '__main__':
    n = 4
    m = 4
    cache = [1, 2, 3, 4]
    print(findMinTime(n, cache))

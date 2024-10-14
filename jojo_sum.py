def find_sum(a, b, c, d):
    # According to the given diamond in the question,
    # we will be adding a 2 times because a/1 + a/1 = 2a
    # We will be adding b 2 times because b/2 + b/2 + b/2 + b/2 = 2b
    # We will be adding c 4/3 times because c/3 + c/3 + c/3 + c/3 = 4c/3
    # We will be adding d 1/2 times because d/4 + d/4 = d/2

    return 2*a + 2*b + 4*c/3 + d/2


if __name__ == '__main__':
    T = int(input())
    results = []
    for _ in range(T):
        a, b, c, d = map(int, input().split())
        results.append(find_sum(a, b, c, d))

    for res in results:
        print('{:.2f}'.format(res))

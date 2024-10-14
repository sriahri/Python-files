def minimumDifference(laddus, n, k):
    # Initialize a variable to largest number
    minimum = 99999999999999999999
    for i in range(n - k + 1):
        # Getting minimum from all the possible subsets.
        minimum = min(minimum , (laddus[i+k-1] - laddus[i]))
    return minimum

for _ in range(int(input())):
    n, k = map(int,input().split())
    l = list(map(int,input().split()))
    # Sort the list.
    l.sort()
    print(minimumDifference(l,n,k))
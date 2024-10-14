for _ in range(int(input())):
    n = int(input())
    r = list(map(int,input().split()))
    d = {}
    maxi = -99999999
    for i in range(1, n+1):
        d[i] = sum(r[i-1::i])
        if d[i] > maxi:
            maxi = d[i]
    mini = n+1
    for i in d.keys():
        if d[i] == maxi and i < mini:
            mini = i
    print(mini)
n, c, m = map(int,input().split())
if n < c:
    print(0)
chocolates = n//c
chocolates += (chocolates - 1)//(m-1)
print(chocolates)
n = int(input())
l = list(map(int,input().split()))
s = ''.join(l)
key = int(input())
x = s.find(str(key))
if x == -1:
    print(-1)
if x == len(l) -1:
    print(-2)
else:
    print(x,l[x+1])
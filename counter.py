n=int(input())
a=0
l=list(map(int,input().split()))
x=int(input())
s=[]
for i in range(x):
    s.append(input().split())
for i in range(x):
    if s[i][0] in l:
        a+=s[i][1]
        t=l.index(s[i][0])
        l.pop(t)
print(a)

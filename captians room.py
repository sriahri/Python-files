n=int(input())
l=list(map(int,input().split()))
s=set(l)
x=list(s)
y=[]
for i in x:
    y.append(l.count(i))
for i in range(len(y)):
    if y[i]!=n:
        a=i
print(x[i])

n=int(input())
l=[]
for i in range(n):
    x=[]
    for j in range(1):
        x.append(input())
        x.append(float(input()))
    l.append(x)
s=sorted(l,key=lambda x:x[1])
o=s[0][1]
p=1
r=0
for i in range(1,n):
    if s[i][1]==o:
        p+=1
q=s[0+p][1]
for i in range(p,n):
    if s[i][1]==q:
        r+=1
y=[]
for i in range(r):
    y.append(s[0+p+i][0])
y.sort()
for i in y:
    print(i)

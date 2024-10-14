n=int(input())
l=[]
x=[]
s=[]
y=[]
t=[]
for i in range(n):
    l.append(input())
    y.append(float(input()))
for i in y:
    s.append(i)
y.sort()
for i in y[::-1]:
    x.append(i)
o=y.count(x[0])
p=y.count(x[0+o])
while s.index(x[0+o])!=-1:
    i=s.index(x[0+o])
    t.append(l[i])
    i+=1
t.sort()
for i in t:
    print(i)




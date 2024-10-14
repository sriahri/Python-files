s=input()
l=[]
for i in s:
    l.append(int(i))
x=[]
for i in l:
    c=1
    if i==i+1:
        c+=1
    x.append(c)
for i in range(len(l)):
    for j in range(len(l)):
        t=tuple(x[j],l[i])
        print(t,end='')
        

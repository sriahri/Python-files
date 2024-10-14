s=input()
k=int(input())
l=[]
i=0
while s[i]!='\o':
    x=''
    for j in range(k):
        x+=s[i+j]
        i+=k
    l.append(x)
for i in range(len(l)):
    y=''
    for j in range(1,len(s)//k):
        if l[i][j]!=l[i][j-1]:
            y+=l[i][j]+l[i][j-1]
    print(y)
            

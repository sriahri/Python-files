r=int(input())
c=int(input())
x=[]
l=[[int(input())for i in range(r)]for j in range(c)]
for i in range(r):
    y=[]
    for j in range(c):
        y.append(0)
    x.append(y)
for i in range(r):
    for j in range(c):
        x[i][j]=l[j][i]
        print(x[i][j])

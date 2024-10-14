s=set(map(int,input().split()))
n=int(input())
#l=[set(map(int,input().split()))for i in range(n)]
l=[]
for i in range(n):
    l.append(set(map(int,input().split())))
x=[]
for i in range(n):
    x.append(s>l[i])
for i in range(len(x)):
    if x[i]==0:
        print('False')
        break
else:
    print('True')


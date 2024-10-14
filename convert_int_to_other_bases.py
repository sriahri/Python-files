s = ''
def convert(n,x):
    global s
    while n > 0:
        s += str(n%x)
        n = n//x
n = int(input())
x = int(input())
convert(n,x)
o = s
l = len(o)
c = 0
r = 0
if '0' not in o:
    r = -1
else:
    for i in range(l):
        if o[i] == '1':
            c = 0
        else:
            c += 1
            r = max(r,c)
print(r)
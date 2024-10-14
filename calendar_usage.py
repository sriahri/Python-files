import math as m
import cmath as c
s=input().split('+')
x=s[1]
d=''
for i in x:
    if i=='j':
        pass
    else:
        d+=i
y=float(s[0])
z=float(d)
n=complex(y,z)
o=m.sqrt(y**2+z**2)
p=c.phase(n)
print('%.3f'%o)
print('%.3f'%p)


from math import gcd
n = int(input())
points = []
l = list(map(int, input().split()))
i = 0
while(i < 2*n):
    points.append([l[i], l[i+1]])
    i += 2
diffy = points[1][1] - points[0][1]
diffx = points[1][0] - points[0][0]
m = diffy/diffx
cmd = gcd(diffx, diffy)
slope = (diffy//cmd)/(diffx//cmd)
c = diffy - slope*diffx

for i in points[2:]:
    if float(i[1]) != ((slope * i[0] + c)):
        print(0)
        break
else:    
    if slope > 0:
        print(str(diffx) + 'x' + '-' + str(diffy) + 'y='+str(int(c))) 
    else:
        print(str(diffx) + 'x' + '+' + str(-1 * diffy) + 'y='+str(int(c))) 
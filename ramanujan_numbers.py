import sys
import stdio

n = int(sys.argv[1])
a = 1
while a*a*a <= n:
    b = a + 1
    while b*b*b <= n:
        c = a + 1
        while c*c*c <= n:
            d = c + 1
            while d*d*d <= (n-c*c*c):
                if a*a*a + b*b*b == c*c*c + d*d*d:
                    x = a*a*a + b*b*b
                    y = c*c*c + d*d*d
                    stdio.write(str(x)+'=')
                    stdio.write(str(a)+'^3 + '+str(b)+'^3 = ')
                    stdio.writeln(str(c)+'^3 + '+str(d)+'^3')
                d += 1
            c += 1
        b += 1
    a += 1
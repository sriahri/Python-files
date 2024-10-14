s1 = input()
s2 = input()
n = len(s1)
n2 = len(s2)
c = 0
for i in range(n):
    if s1[i:i+n2] == s2:
        c += 1
        i = i+n2
print(c)
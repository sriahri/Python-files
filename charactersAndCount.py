from collections import Counter
s = input()
d = Counter(s)
res = ''
for i in sorted(d.keys()):
   res += i+str(d[i])
print(res)
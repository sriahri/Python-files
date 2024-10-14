n, m = map(int, input().split())
l = []
for i in range(m):
    l.append(list(map(int,input().split())))
x = set(l[0][0])
y = set(l[0][1])
x.add(y)
res = set(x)
for i in l[1:]:
    for j in res:
        if i[0] in j:
            j.add(i[0])
            j.add(i[1])
    res.remove(j)
    res.add(j)
mini = n
for i in list(res):
    mini = min(mini, len(list(i)))
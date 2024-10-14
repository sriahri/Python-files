from heapq import heapify, heappop

n, k, c = map(int, input().split())
teams = {}
ranks = []
heap1 = []
for i in range(n):
    t, s = map(int, input().split())
    teams[t] = s
    ranks.append(t)
    heap1.append((i, t, s))

res = []
d = {}
heapify(heap1)
for i in list(teams.keys()):
    d[teams[i]] = 0

heap2 = []
while heap1 and len(res) < k:
    i, t, s = heappop(heap1)
    if d[s] < c:
        d[s] += 1
        res.append((i, t))
    else:
        heap2.append((i, t, s))

heapify(heap2)

for i in range(k - len(res)):
    i, t, s = heappop(heap2)
    res.append((i, t))

res.sort()
for i, j in res:
    print(j)

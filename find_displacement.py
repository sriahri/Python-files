def distanceTravel(N, Q, U, A, Queries):
    displacement = 0
    for i in range(Q):
        l = Queries[i][0]
        r = Queries[i][1]
        t1 = Queries[i][2]
        t2 = Queries[i][3]
        for i in range(l-1, r):
            s = (t2-t1)*(U[i] + (A[i]*(t2+t1))//2)
            displacement += s
    return displacement%(1000000007)

n = int(input())
q = int(input())
u = []
for i in range(n):
    u.append(int(input()))
    
a = []
for i in range(n):
    a.append(int(input()))
    
queries = []
for i in range(q):
    queries.append(list(map(int, input().split())))
print(u)
print(n)
print(q)
print(a)
print(queries)
print(distanceTravel(n, q, u, a,queries))
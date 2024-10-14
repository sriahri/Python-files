from collections import defaultdict,deque
def function(n, m, s, p, q):
    s = list(s)
    directed_edge_graph=[0 for i in range(n)]
    graph=defaultdict(list)
    for i in range(m):
        a,b=p[i], q[i]
        a-=1
        b-=1
        graph[a].append(b)
        directed_edge_graph[b]+=1
    q=deque()
    for i in range(n):
        if directed_edge_graph[i]==0:
            q.append(i)
    count=0
    ans=0
    dp=[[0 for i in range(26)] for i in range(n)]
    while count<n and q:
        und=q.popleft()
        count+=1
        dp[und][ord(s[und])-97]+=1
        for i in graph[und]:
            for j in range(26):
                dp[i][j]=max(dp[i][j],dp[und][j])
            directed_edge_graph[i]-=1
            if directed_edge_graph[i]==0:
                q.append(i)
    if count!=n:
        return -1
    else:
        ans=0
        for i in range(n):
            ans=max(ans,max(dp[i]))
        return ans

# n = int(input())
# m = int(input())
# s = input()
# p = list(map(int,input().split()))
# q = list(map(int,input().split()))
# print(function(n, m, s, p, q))


test_list = [(1, 1, 'a', [1],[1], -1), (5, 4, 'abaca', [1, 1, 3, 4], [2, 3, 4, 5], 3), (6, 6, 'xyzabc', [1, 3, 2, 5, 4, 6], [2, 1, 3, 4, 3, 4], -1)]

for n, m, s, p, q, res in test_list:
    assert function(n, m, s, p, q) == res
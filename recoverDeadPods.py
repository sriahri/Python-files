class Graph:

    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]

    def DFSUtil(self, temp, v, visited):
        visited[v] = True
        temp.append(v)
        for i in self.adj[v]:
            if not visited[i]:
                temp = self.DFSUtil(temp, i, visited)
        return temp

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        for v in range(self.V):
            if not visited[v]:
                temp = []
                cc.append(self.DFSUtil(temp, v, visited))
        return cc


def recoverDeadPods(n, connections, queries):
    g = Graph(n)
    for connection in connections:
        g.addEdge(connection[0]-1, connection[1]-1)

    result = g.connectedComponents()

    lost_connection = []
    final_result = []
    for query in queries:
        if query[0] == 2:
            lost_connection.append(query[1])
        else:
            if query[1] not in lost_connection:
                final_result.append(query[1])
            else:
                for pods in result:
                    if query[1] in pods:
                        min_pod = 99999999999
                        for pod in pods:
                            if pod not in lost_connection and min_pod > pod:
                                min_pod = pod
                if min_pod == 99999999999:
                    min_pod = -2
                final_result.append(min_pod+1)
    return final_result


if __name__ == '__main__':
    n = int(input().strip())
    recoverDeadPods()
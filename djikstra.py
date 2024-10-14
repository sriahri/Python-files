import sys

MAX_INT = sys.maxsize


class Algorithm:
    def __init__(self):
        self.path = []
        self.distance = 0
        self.via = ""

    def Dijkstra(self, graph, source, destination):
        size = len(graph[0])
        self.path.append(source)
        parent = [-1 for _ in range(size)]
        markedVertex = [False for _ in range(size)]
        distances = [MAX_INT for _ in range(size)]
        distances[source] = 0
        for i in range(size - 1):
            mini = self.getMinimumDistance(distances, markedVertex, size)
            markedVertex[mini] = True
            for j in range(size):
                if (not markedVertex[j]) and graph[mini][j] != 0 and distances[mini] != MAX_INT and distances[mini] + \
                        graph[mini][j] < distances[j]:
                    parent[j] = mini
                    distances[j] = distances[mini] + graph[mini]
        self.getActualDistances(distances, parent, source, destination, size)

    def getMinimumDistance(self, distances, markedVertex, size):
        min_index = -1
        maximum = MAX_INT
        for i in range(size):
            if markedVertex[i] == False and distances[i] <= maximum:
                maximum = distances[i]
                min_index = i
        return min_index

    def getActualDistances(self, distances, parent, source, destination, size):
        for k in range(size):
            if k == destination:
                distance = distances[k]
                self.printPath(parent, k, destination)
        self.printIt(self.path, destination)

    def printPath(self, parent, x, destination):
        if parent[x] == -1:
            return
        self.printPath(parent, parent[x], destination)
        if x == destination:
            return
        self.path.append(x)

    def printIt(self, path, destination):
        self.path.append(destination)
        for l in range(len(self.path)):
            self.via += " " + path[l]

    def reset(self):
        self.path.clear()
        self.distance = 0
        self.via = ""

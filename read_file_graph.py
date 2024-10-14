def readGraph():
    file = open('graph.txt') # Open file
    lines = file.readlines() # Read all lines from file
    vertices = len(lines) # No. of vertices
    # Adjacency matrix declared
    adj_matrix = [[0 for i in range(vertices)]for j in range(vertices)]
    k = 0
    for i in range(vertices):
        nodes = lines[i].split('->') # Split nodes for the vertex
        k = 0
        for j in range(vertices):
            if i != j:
                # Split each node and weight
                node, weight = map(int, nodes[k].split())
                adj_matrix[i][node] = weight
                k += 1
    # Print the adjacency matrix
    for i in range(vertices):
        for j in range(vertices):
            if j == vertices - 1:
                print(adj_matrix[i][j])
            else:
                print(adj_matrix[i][j], end = ', ')
readGraph()
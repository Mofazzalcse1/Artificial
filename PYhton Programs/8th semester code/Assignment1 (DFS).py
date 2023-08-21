from collections import defaultdict
from collections import deque


class Graph:
    def __init__(self, directed):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdges(self, x, y):
        if self.directed:
            self.graph[x].append(y)
        else:
            self.graph[x].append(y)
            self.graph[y].append(x)

    def DFS(self, vertex):
        visited = []
        stack = deque()
        stack.append(vertex)

        while len(stack) != 0:
            vertex = stack.pop()
            if vertex in visited:
                continue
            print(vertex, end=" ")
            visited.append(vertex)

            for neighbour in self.graph[vertex]:
                stack.append(neighbour)


g = Graph(True)

g.addEdges('A', 'B')
g.addEdges('A', 'C')
g.addEdges('B', 'C')
g.addEdges('B', 'D')
g.addEdges('B', 'E')
g.addEdges('C', 'F')
g.addEdges('D', 'G')
g.addEdges('E', 'C')
g.addEdges('E', 'D')
g.addEdges('E', 'F')
g.addEdges('E', 'G')
g.addEdges('E', 'H')
g.addEdges('F', 'H')
g.addEdges('G', None)
g.addEdges('H', 'G')

g.graph


g.DFS('A')

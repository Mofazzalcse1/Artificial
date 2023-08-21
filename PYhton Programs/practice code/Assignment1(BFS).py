from collections import defaultdict
from queue import Queue


class Graph():
    def __init__(self, directed):
        self.graph = defaultdict(list)
        self.directed = directed

    def addEdges(self, x, y):
        if self.directed:
            self.graph[x].append(y)
        else:
            self.graph[x].append(y)
            self.graph[y].append(x)

    def BFS(self, vertex):
        visited = []
        queue = Queue()
        queue.put(vertex)

        while not queue.empty():
            vertex = queue.get()
            if vertex in visited:
                continue
            print(vertex, end="")
            visited.append(vertex)

            for neighbour in self.graph[vertex]:
                if neighbour is not None:
                    queue.put(neighbour)


g = Graph()



from collections import defaultdict
from queue import PriorityQueue


class Graph:
    def __init__(self, directed):

        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, a, b, cost):

        if self.directed:
            value = (cost, b)
            self.graph[a].append(value)
        else:
            value = (cost, b)
            self.graph[a].append(value)
            value = (cost, a)
            self.graph[b].append(value)

    def ucs(self, start_node, goal_node):

        visited = []
        queue = PriorityQueue()
        queue.put((0, start_node))

        while not queue.empty():
            item = queue.get()
            start_node = item[1]

            if start_node == goal_node:
                print(start_node, end=" ")
                queue.queue.clear()
            else:
                if start_node in visited:
                    continue

                print(start_node, end=" ")
                visited.append(start_node)

                for neighbour in self.graph[start_node]:
                    queue.put((neighbour[0], neighbour[1]))


g = Graph(True)
g.graph = defaultdict(list)

g.add_edge('S', 'A', 5)
g.add_edge('S', 'B', 9)
g.add_edge('S', 'D', 6)
g.add_edge('A', 'B', 3)
g.add_edge('A', 'G1', 9)
g.add_edge('B', 'A', 2)
g.add_edge('B', 'C', 1)
g.add_edge('C', 'G2', 5)
g.add_edge('C', 'F', 7)
g.add_edge('C', 'S', 6)
g.add_edge('D', 'C', 2)
g.add_edge('D', 'E', 2)
g.add_edge('E', 'G3', 7)
g.add_edge('F', 'G3', 8)
g.add_edge('F', 'D', 2)

defaultdict(list,
            {'S': [(5, 'A'), (9, 'B'), (6, 'D')],
             'A': [(3, 'B'), (9, 'G1')],
             'B': [(2, 'A'), (1, 'C')],
             'C': [(5, 'G2'), (7, 'F')],
             'D': [(2, 'C'), (2, 'E')],
             'E': [(7, 'G3')],
             'F': [(8, 'G3'), (2, 'D')],
             })

g.ucs('S', 'G2')
print()
g.ucs('S', 'G1')
print()
g.ucs('S', 'G3')

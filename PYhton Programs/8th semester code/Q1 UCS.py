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

                print(start_node, end="->")
                visited.append(start_node)

                for neighbour in self.graph[start_node]:
                    queue.put((neighbour[0], neighbour[1]))


g = Graph(True)
g.graph = defaultdict(list)

g.add_edge('S', 'A', 1)
g.add_edge('S', 'C', 2)
g.add_edge('S', 'E', 6)

g.add_edge('A', 'B', 3)
g.add_edge('A', 'C', 1)

g.add_edge('B', 'D', 3)

g.add_edge('C', 'G', 2)
g.add_edge('C', 'D', 1)

g.add_edge('D', 'G', 4)

g.add_edge('E', 'G', 6)

defaultdict(list,
            {'S': [(1, 'A'), (2, 'C'), (6, 'E')],
             'A': [(3, 'B'), (1, 'C')],
             'B': [(3, 'D')],
             'C': [(2, 'G'), (1, 'D')],
             'D': [(4, 'G')],
             'E': [(6, 'G')],

             })

g.ucs('S', 'G')


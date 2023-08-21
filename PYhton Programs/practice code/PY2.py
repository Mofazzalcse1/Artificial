# num1 = 25
# num2 = 35
# # if num1 <= num2:
# #     print(num2)
# # else:
# #     print(num1)
#
# max = num1 if num1 > num2 else num2
# print(max)


from collections import defaultdict
from queue import PriorityQueue


class Graph:
    def __init__(self, directed):

        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self, u, v, weight):

        if self.directed:
            value = (weight, v)
            self.graph[u].append(value)
        else:
            value = (weight, v)
            self.graph[u].append(value)
            value = (weight, u)
            self.graph[v].append(value)

    def ucs(self, current_node, goal_node):

        visited = []
        queue = PriorityQueue()
        queue.put((0, current_node))

        while not queue.empty():
            item = queue.get()
            current_node = item[1]

            if current_node == goal_node:
                print(current_node, end=" ")
                queue.queue.clear()
            else:
                if current_node in visited:
                    continue

                print(current_node, end=" ")
                visited.append(current_node)

                for neighbour in self.graph[current_node]:
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

# g.ucs('S', 'G1')
g.ucs('S', 'G2')
# g.ucs('S', 'G3')

# from collections import defaultdict
# from queue import PriorityQueue
#
#
# class Graph:
#     def __init__(self, directed):
#         self.graph = defaultdict(list)
#         self.directed = directed
#
#     def addEdges(self, u, v, weight):
#         if self.directed:
#             value = (v, weight)
#             self.graph[u].append(v)
#         else:
#             value = (v, weight)
#             self.graph[u].append(v)
#             value = (u, weight)
#             self.graph[v].append(u)
#
#     def UCS(self, start_node, goal_node):
#         visited = []
#         queue = PriorityQueue()
#         queue.put((0, start_node))
#
#         while not queue.empty():
#             item = queue.get()
#             start_node = item[1]
#             if start_node == goal_node:
#                 print(start_node, end="")
#                 queue.queue.clear()
#             else:
#                 if start_node in visited:
#                     continue
#                 print(start_node, end="")
#                 visited.append(start_node)
#                 for neighbour in self.graph[start_node]:
#                     queue.put((neighbour[0], neighbour[1]))
#
#
# g = Graph(True)
#
# g.graph = defaultdict(list)
#
# g.addEdges('S', 'A', 5)
# g.addEdges('S', 'B', 9)
# g.addEdges('S', 'D', 6)
# g.addEdges('A', 'B', 3)
# g.addEdges('A', 'G1', 9)
# g.addEdges('B', 'A', 2)
# g.addEdges('B', 'C', 1)
# g.addEdges('C', 'G2', 5)
# g.addEdges('C', 'F', 7)
# g.addEdges('C', 'S', 6)
# g.addEdges('D', 'C', 2)
# g.addEdges('D', 'E', 2)
# g.addEdges('E', 'G3', 7)
# g.addEdges('F', 'G3', 8)
# g.addEdges('F', 'D', 2)
#
# start = g.graph
# print(start)
#
# g.UCS('S', 'G1')
# g.UCS('S', 'G2')
# g.UCS('S', 'G3')
#
#
#

# 2. Do a program for chemical reaction problem where the initials of chemicals and time shall be taken as input.
# User should be able to take input of time interval and constants. Do the program using function calling.

def uniform_cost_search(goal, start):
    global graph, cost
    answer = []

    queue = []

    for i in range(len(goal)):
        answer.append(10 ** 8)

    queue.append([0, start])

    visited = {}

    # count
    count = 0

    while len(queue) > 0:

        queue = sorted(queue)
        p = queue[-1]

        del queue[-1]

        p[0] *= -1

        if p[1] in goal:

            index = goal.index(p[1])

            if answer[index] == 10 ** 8:
                count += 1

            if answer[index] > p[0]:
                answer[index] = p[0]

            del queue[-1]

            queue = sorted(queue)
            if count == len(goal):
                return answer

        if p[1] not in visited:
            for i in range(len(graph[p[1]])):
                queue.append([(p[0] + cost[(p[1], graph[p[1]][i])]) * -1, graph[p[1]][i]])

        visited[p[1]] = 1

    return answer


# main function
if __name__ == '__main__':
    # create the graph
    graph, cost = [[] for i in range(8)], {}

    # add edge
    graph[0].append(1)
    graph[0].append(3)
    graph[3].append(1)
    graph[3].append(6)
    graph[3].append(4)
    graph[1].append(6)
    graph[4].append(2)
    graph[4].append(5)
    graph[2].append(1)
    graph[5].append(2)
    graph[5].append(6)
    graph[6].append(4)

    # add the cost
    cost[(0, 1)] = 2
    cost[(0, 3)] = 5
    cost[(1, 6)] = 1
    cost[(3, 1)] = 5
    cost[(3, 6)] = 6
    cost[(3, 4)] = 2
    cost[(2, 1)] = 4
    cost[(4, 2)] = 4
    cost[(4, 5)] = 3
    cost[(5, 2)] = 6
    cost[(5, 6)] = 3
    cost[(6, 4)] = 7

    # goal state
    goal = [6]

    # set the goal
    # there can be multiple goal states

    # get the answer
    answer = uniform_cost_search(goal, 0)

    print("Minimum cost from 0 to 6 is = ", answer[0])

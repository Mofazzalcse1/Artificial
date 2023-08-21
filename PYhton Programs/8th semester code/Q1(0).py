from queue import PriorityQueue


class Node(object):

    def __init__(self, label: str = None):
        self.label = label
        self.children = []

    def __lt__(self, other):
        return self.label < other.label

    def __gt__(self, other):
        return self.label > other.label

    def __repr__(self):
        return '{} -> {}'.format(self.label, self.children)

    def add_child(self, node, cost=1):
        edge = Edge(self, node, cost)
        self.children.append(edge)


class Edge(object):

    def __init__(self, source: Node, destination: Node, cost: int = 1):
        self.source = source
        self.destination = destination
        self.cost = cost

    def __repr__(self):
        return '{}: {}'.format(self.cost, self.destination.label)


S = Node('S')
A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
G = Node('G')

S.add_child(A, 1)
S.add_child(C, 2)
S.add_child(E, 6)

A.add_child(B, 3)
A.add_child(C, 1)

B.add_child(D, 3)

C.add_child(D, 1)
C.add_child(G, 2)

D.add_child(G, 4)
E.add_child(G, 6)

_ = [print(node) for node in [S, A, B, C, D, E, G]]


def ucs(root, goal):
    queue = PriorityQueue()
    queue.put((0, [root]))

    while not queue.empty():

        pair = queue.get()
        current = pair[1][-1]

        if current.label == goal:
            return pair[1]

        for edge in current.children:
            new_path = list(pair[1])
            new_path.append(edge.destination)

            queue.put((pair[0] + edge.cost, new_path))


ucs(S, 'G')

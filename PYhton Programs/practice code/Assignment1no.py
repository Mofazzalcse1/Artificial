graph = {
    'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'D': ['G'], 'E': ['H'], 'F': [], 'G': [], 'H': []
}

visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print("Following is the DFS")
dfs(visited, graph, 'A')

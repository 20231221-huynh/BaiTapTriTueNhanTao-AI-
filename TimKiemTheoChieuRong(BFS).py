from collections import deque

graph = {
    'A': ['C', 'D', 'F'],
    'C': ['B', 'E'],
    'D': ['G'],
    'F': [],
    'B': [],
    'E': [],
    'G': ['H', 'T'],
    'H': ['K', 'M'],
    'K': [],
    'M': [],
    'T': []
}

queue = deque(['A'])
visited = {'A'}
parent = {'A': None}

while queue:
    u = queue.popleft()

    if u == 'T':
        break

    for v in graph[u]:
        if v not in visited:
            visited.add(v)
            parent[v] = u
            queue.append(v)

path = []
u = 'T'

while u is not None:
    path.append(u)
    u = parent[u]

path.reverse()

print("Đường đi:", " -> ".join(path))

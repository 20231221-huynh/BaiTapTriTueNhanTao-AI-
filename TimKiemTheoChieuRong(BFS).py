from collections import deque

graph = {
    'A': ['B', 'C', 'D'],
    'B': ['E', 'F'],
    'C': ['G', 'H'],
    'D': ['I', 'J'],
    'E': ['K', 'L'],
    'F': ['L', 'M'],
    'G': ['N'],
    'H': ['O', 'P'],
    'I': ['P', 'Q'],
    'J': ['N'],
    'K': ['S'],
    'L': ['T'],
    'M': [],
    'N': [],
    'O': [],
    'P': ['U'],
    'Q': [],
    'S': [],
    'T': [],
    'U': []
}

def bfs_search(graph, start, goal):
    visited = []
    queue = deque([start])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            
            if node == goal:
                break

            for neighbor in graph.get(node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
                    
    return visited

result = bfs_search(graph, 'A', 'P')
print("Thứ tự các nút duyệt qua (BFS):")
print(" -> ".join(result))

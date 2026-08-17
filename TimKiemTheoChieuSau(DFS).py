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

def dfs_search(graph, start, goal):
    visited = []
    stack = [start]
    
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            
            if node == goal:
                break
                
            for neighbor in reversed(graph.get(node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
                    
    return visited

result = dfs_search(graph, 'A', 'P')
print("Thứ tự các nút duyệt qua (DFS):")
print(" -> ".join(result))

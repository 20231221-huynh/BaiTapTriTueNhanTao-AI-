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

def dls_search(graph, start, goal, max_depth):
    visited = []
    
    def dfs_limit(node, depth):
        if depth > max_depth or node in visited:
            return False
        
        visited.append(node)
        
        if node == goal:
            return True
            
        if depth < max_depth:
            for neighbor in graph.get(node, []):
                if dfs_limit(neighbor, depth + 1):
                    return True
        return False

    dfs_limit(start, 0)
    return visited

result = dls_search(graph, 'A', 'P', max_depth=3)
print("Thứ tự các nút duyệt qua (DFS với độ sâu = 3):")
print(" -> ".join(result))

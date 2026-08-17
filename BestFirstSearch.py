graph = {
    'A': ['C', 'D', 'E'],
    'C': ['F'],
    'D': ['F', 'I'],
    'E': ['K', 'G'],
    'F': ['B'],
    'I': ['B', 'G'],
    'G': ['B', 'H'],
    'K': [],
    'H': ['B'],
    'B': []
}

h = {
    'A': 20,
    'B': 0,
    'C': 15,
    'D': 6,
    'E': 7,
    'F': 10,
    'G': 5,
    'H': 3,
    'I': 8,
    'K': 12
}


def best_first_search(start, goal):

    OPEN = [start]
    CLOSED = []

    path = []

    while OPEN:

        current = min(OPEN, key=lambda x: h[x])

        print("OPEN:", [(x, h[x]) for x in OPEN])
        print("Chọn:", current)

        path.append(current)

        if current == goal:
            return path

        OPEN.remove(current)
        CLOSED.append(current)

        for neighbor in graph[current]:

            if neighbor not in OPEN and neighbor not in CLOSED:
                OPEN.append(neighbor)

    return None


path = best_first_search('A', 'B')

print("Đường đi:", " -> ".join(path))

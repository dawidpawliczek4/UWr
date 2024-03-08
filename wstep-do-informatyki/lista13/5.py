from collections import deque

def shortest_path_and_length(graph, start, end):
    # Sprawdź, czy wierzchołki start i end istnieją w grafie
    if start not in graph or end not in graph:
        return -1, []

    # Kolejka do przeszukiwania BFS i śledzenie długości ścieżki
    queue = deque([(start, 0)])
    # Słownik do przechowywania odwiedzonych wierzchołków i ich rodziców
    visited = {start: None}
    
    # BFS do znalezienia najkrótszej ścieżki
    while queue:
        current, length = queue.popleft()
        if current == end:
            break
        for neighbor in graph[current]:
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append((neighbor, length + 1))
    
    # Jeżeli nie odwiedziliśmy końca, to nie ma ścieżki
    if end not in visited:
        return -1, []
    
    # Odtwórz ścieżkę od końca do początku
    path = []
    while end is not None:
        path.append(end)
        end = visited[end]
    path.reverse()  # Odwróć ścieżkę, aby była od startu do końca

    return length, path

# Przykładowy graf skierowany w postaci słownika list sąsiedztwa
graph_example = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Przykładowe wywołanie funkcji dla wierzchołków 'A' i 'F'
e = shortest_path_and_length(graph_example, 'A', 'F')
print(e)
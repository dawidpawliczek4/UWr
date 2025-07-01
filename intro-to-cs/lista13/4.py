from collections import deque

def find_path(graph, start, end):
    # Sprawdź, czy wierzchołki start i end istnieją w grafie
    if start not in graph or end not in graph:
        return None

    # Kolejka do przeszukiwania BFS
    queue = deque([start])
    # Słownik do przechowywania rodziców w celu odtworzenia ścieżki
    parents = {start: None}
    # Znajdź ścieżkę przy użyciu BFS
    while queue:
        vertex = queue.popleft()
        if vertex == end:
            break
        for neighbor in graph[vertex]:
            if neighbor not in parents:  # Nie odwiedzaj wierzchołka, jeśli już ma rodzica (czyli był odwiedzony)
                parents[neighbor] = vertex  # Ustaw rodzica dla sąsiada
                queue.append(neighbor)

    # Jeśli end nie ma rodzica, to nie istnieje ścieżka
    if end not in parents:
        return None

    # Odtwórz ścieżkę od końca do początku
    path = []
    while end is not None:
        path.append(end)
        end = parents[end]
    path.reverse()  # Odwróć ścieżkę, aby była od startu do końca

    return path

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
e = find_path(graph_example, 'A', 'F')
print(e)

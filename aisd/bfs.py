from collections import deque

def bfs(graph, start):
    """
    Przeszukiwanie wszerz – iteracyjna wersja.
    
    :param graph: słownik, gdzie klucze to wierzchołki, a wartości to listy sąsiadów
    :param start: wierzchołek początkowy
    :return: lista wierzchołków w kolejności odwiedzin
    """
    visited = set([start])
    result = []
    queue = deque([start])
    
    while queue:
        vertex = queue.popleft()
        result.append(vertex)
        # Przeglądamy sąsiadów bieżącego wierzchołka
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return result


# Przykładowe użycie BFS:
graph_example = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print("BFS:", bfs(graph_example, 'A'))

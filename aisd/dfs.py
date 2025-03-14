def dfs_recursive(graph, start, visited=None):
    """
    Przeszukiwanie w głąb – rekurencyjna wersja.
    
    :param graph: słownik, gdzie klucze to wierzchołki, a wartości to listy sąsiadów
    :param start: wierzchołek początkowy
    :param visited: zbiór odwiedzonych wierzchołków (używany wewnętrznie)
    :return: lista wierzchołków w kolejności odwiedzin
    """
    if visited is None:
        visited = set()
    # Dodajemy bieżący wierzchołek do zbioru odwiedzonych
    visited.add(start)
    result = [start]
    # Przechodzimy rekurencyjnie do sąsiadów, którzy nie zostali odwiedzeni
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            result.extend(dfs_recursive(graph, neighbor, visited))
    return result

# Przykładowe użycie DFS rekurencyjnego:
graph_example = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print("DFS (rekurencyjnie):", dfs_recursive(graph_example, 'A'))

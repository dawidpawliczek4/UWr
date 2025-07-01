def dfs(graph, start, visited=None):
    """
    Algorytm DFS (przeszukiwanie w głąb) dla grafu reprezentowanego jako lista sąsiedztwa.

    :param graph: Dict, gdzie klucze to wierzchołki, a wartości to listy sąsiednich wierzchołków.
    :param start: Wierzchołek początkowy.
    :param visited: Zbiór odwiedzonych wierzchołków.
    :return: Zbiór odwiedzonych wierzchołków.
    """
    if visited is None:
        visited = set()
    
    # Oznacz bieżący wierzchołek jako odwiedzony
    visited.add(start)
    
    # Dla każdego sąsiada bieżącego wierzchołka
    for neighbor in graph[start]:
        if neighbor not in visited:
            # Rekurencyjnie odwiedzaj sąsiednie wierzchołki
            dfs(graph, neighbor, visited)
    
    return visited


# Przykład użycia
if __name__ == "__main__":
    # Graf reprezentowany jako lista sąsiedztwa
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    start_node = 'A'
    visited_nodes = dfs(graph, start_node)
    print("Odwiedzone wierzchołki:", visited_nodes)

def has_source_vertex(D):
    n = len(D)  # Number of vertices
    
    for i in range(n):
        is_source = True
        
        # Check outgoing edges in row i
        for j in range(n):
            if i != j and D[i][j] == 0:  # Must have outgoing edges to all other vertices
                is_source = False
                break
        
        # Check no incoming edges in column i
        for j in range(n):
            if i != j and D[j][i] == 1:  # Must have no incoming edges
                is_source = False
                break
        
        if is_source:
            return True  # Source vertex found
    
    return False  # No source vertex

# Example usage
D = [
    [0, 1, 1],
    [0, 0, 0],
    [0, 1, 0]
]
print("Contains source vertex:", has_source_vertex(D))


def znajdz_zrodlo(n, graf):
    stopien_wejsciowy = [0] * n  # Stopnie wejściowe dla każdego wierzchołka

    # Obliczanie stopni wejściowych
    for u in range(n):
        for v in graf[u]:
            stopien_wejsciowy[v] += 1

    # Szukanie kandydata na źródło
    for i in range(n):
        if stopien_wejsciowy[i] == 0:  # Brak krawędzi wchodzących
            # Sprawdzenie czy wychodzą łuki do wszystkich innych wierzchołków
            if len(graf[i]) == n - 1:
                return True  # Znaleziono źródło
    return False

# Przykład użycia: graf skierowany z listą sąsiedztwa
n = 4
graf = [
    [1, 2, 3],  # Wierzchołek 0 -> łuki do 1, 2, 3
    [],         # Wierzchołek 1
    [],         # Wierzchołek 2
    []          # Wierzchołek 3
]
print("Czy graf zawiera źródło:", znajdz_zrodlo(n, graf))

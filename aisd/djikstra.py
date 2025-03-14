import heapq

def dijkstra(graph: dict[str, Any], start):
    """
    Oblicza najkrótsze ścieżki z wierzchołka 'start' do wszystkich innych w grafie.
    
    Parametry:
      graph: słownik, gdzie klucze to wierzchołki, a wartości to listy krotek (v, w),
             gdzie 'v' jest sąsiadem, a 'w' wagą krawędzi (u, v).
      start: wierzchołek początkowy.
      
    Zwraca:
      distances: słownik, w którym distances[v] jest najkrótszą odległością od 'start' do 'v'.
      predecessors: słownik, który pozwala odtworzyć ścieżkę – dla każdego wierzchołka v
                    predecessors[v] to poprzednik na najkrótszej ścieżce.
    """
    # Inicjalizacja: wszystkie odległości są nieskończone, poza wierzchołkiem startowym.
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Słownik do odtwarzania ścieżki
    predecessors = {node: None for node in graph}
    
    # Kolejka priorytetowa, na której umieszczamy pary (odległość, wierzchołek)
    queue = [(0, start)]
    
    while queue:
        current_distance, u = heapq.heappop(queue)
        
        # Jeżeli znaleziono już lepszą ścieżkę do u, pomijamy ten element
        if current_distance > distances[u]:
            continue
        
        # Relaksacja krawędzi wychodzących z u
        for v, weight in graph.get(u, []):
            distance = current_distance + weight
            if distance < distances[v]:
                distances[v] = distance
                predecessors[v] = u
                heapq.heappush(queue, (distance, v))
    
    return distances, predecessors


graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1)],
    'D': []
}

start_vertex = 'A'
distances, predecessors = dijkstra(graph, start_vertex)

print("Najkrótsze odległości od wierzchołka", start_vertex)
for node in graph:
    print(f"{start_vertex} -> {node}: {distances[node]}")

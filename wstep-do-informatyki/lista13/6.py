def find_articulation_points(graph):
    n = len(graph)  # Liczba wierzchołków
    visited = [False] * n
    disc = [float("Inf")] * n
    low = [float("Inf")] * n
    parent = [-1] * n
    articulation_points = []
    time = 0

    def dfs(u):
        nonlocal time
        visited[u] = True
        disc[u] = low[u] = time
        time += 1
        children = 0

        for v in graph[u]:
            if not visited[v]:
                parent[v] = u
                children += 1
                dfs(v)
                low[u] = min(low[u], low[v])
                # Warunek 1: u jest korzeniem, a liczba dzieci > 1
                if parent[u] == -1 and children > 1:
                    articulation_points.append(u)
                # Warunek 2: u nie jest korzeniem, a najniższy wierzchołek, do którego można dojść z v jest powyżej u
                if parent[u] != -1 and low[v] >= disc[u]:
                    articulation_points.append(u)
            elif v != parent[u]:  # Aktualizuj low value dla u
                low[u] = min(low[u], disc[v])

    for i in range(n):
        if not visited[i]:
            dfs(i)

    return set(articulation_points)  # Usuwamy duplikaty, ponieważ punkt artykulacji może być dodany więcej niż raz

# Przykładowy graf w postaci listy sąsiedztwa, gdzie klucze to indeksy wierzchołków
graph_example = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4],
    4: [3]
}

# Wyszukanie punktów artykulacji w grafie
find_articulation_points(graph_example)

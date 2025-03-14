def build_tree(edges):
    """
    Buduje drzewo w postaci słownika children, gdzie dla każdego wierzchołka 
    podajemy listę jego dzieci oraz zwraca korzeń drzewa.
    
    :param edges: lista krotek (p, a), gdzie p jest rodzicem a.
    :return: (root, children) - root to korzeń drzewa, a children to słownik
             postaci: {wierzchołek: [lista dzieci]}.
    """
    children = {}
    has_parent = {}
    
    # Ustalamy, które wierzchołki mają rodzica
    for p, a in edges:
        if p not in children:
            children[p] = []
        children[p].append(a)
        
        # Zaznaczamy, że a ma rodzica
        has_parent[a] = True
        
        # Upewniamy się, że rodzic p również jest uwzględniony
        if p not in has_parent:
            has_parent[p] = False

    # Znajdujemy korzeń: to ten, który nie ma rodzica (has_parent[v] == False)
    root = None
    for v, parent_flag in has_parent.items():
        if not parent_flag:
            root = v
            break

    # Upewniamy się, że każdy wierzchołek ma przypisaną listę dzieci
    for v in has_parent:
        if v not in children:
            children[v] = []
            
    return root, children

def compute_times(root, children):
    """
    Przeprowadza przeszukiwanie DFS od korzenia i oblicza tablice tin i tout.
    
    :param root: korzeń drzewa.
    :param children: słownik dzieci dla każdego wierzchołka.
    :return: dwie tablice (słowniki) tin i tout, gdzie:
             - tin[v] to "czas wejścia" do wierzchołka v,
             - tout[v] to "czas wyjścia" z wierzchołka v.
    """
    tin = {}
    tout = {}
    time = [0]  # używamy listy jako mutowalnego licznika
    
    def dfs(v):
        time[0] += 1
        tin[v] = time[0]
        for child in children[v]:
            dfs(child)
        time[0] += 1
        tout[v] = time[0]
    
    dfs(root)
    return tin, tout

def is_on_path(v, u, tin, tout):
    """
    Sprawdza, czy wierzchołek v leży na ścieżce od u do korzenia.
    Wykorzystujemy własność DFS: v jest przodkiem u wtedy i tylko wtedy,
    gdy tin[v] <= tin[u] oraz tout[v] >= tout[u].
    
    :param v: potencjalny przodek.
    :param u: wierzchołek, dla którego sprawdzamy, czy v jest przodkiem.
    :param tin: słownik czasów wejścia.
    :param tout: słownik czasów wyjścia.
    :return: True, jeśli v leży na ścieżce (jest przodkiem) u, inaczej False.
    """
    return tin[v] <= tin[u] and tout[v] >= tout[u]

def check_queries(edges, queries):
    """
    Dla danego drzewa (lista krawędzi) oraz listy zapytań (pary (v, u))
    sprawdza, czy v leży na ścieżce od u do korzenia.
    
    :param edges: lista krawędzi (p, a), gdzie p jest rodzicem a.
    :param queries: lista par (v, u).
    :return: lista wyników, gdzie dla każdej pary wypisujemy "TAK" lub "NIE".
    """
    root, children = build_tree(edges)
    tin, tout = compute_times(root, children)
    
    results = []
    for v, u in queries:
        if is_on_path(v, u, tin, tout):
            results.append("TAK")
        else:
            results.append("NIE")
    return results

# Przykładowe użycie:

# Drzewo reprezentowane jako lista krawędzi (rodzic, dziecko)
edges = [
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (3, 6),
    (3, 7)
]

# Lista zapytań w postaci par (v, u)
# Pytanie: czy v leży na ścieżce od u do korzenia?
queries = [
    (1, 4),  # Czy 1 jest przodkiem 4? Odpowiedź: TAK.
    (2, 7),  # Czy 2 jest przodkiem 7? Odpowiedź: NIE.
    (3, 7),  # Czy 3 jest przodkiem 7? Odpowiedź: TAK.
    (2, 2),  # Czy 2 jest przodkiem samego siebie? TAK.
]

results = check_queries(edges, queries)
for query, res in zip(queries, results):
    print(f"Dla pary {query}: {res}")

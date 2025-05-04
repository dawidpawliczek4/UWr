n = 0
kostki = []

with open("200k.in") as fin:
    first = True
    for line in fin:
        if first == True:
            n = line.strip()
            first = False
        else:
            kostka = line.strip().split()            
            kostki.append((int(kostka[0]), int(kostka[1]), int(kostka[2])))




def zbuduj_graf(kostki):
    graf = {}
    for k in kostki:
        l, m, r = k
        if l not in graf:
            graf[l] = []
        graf[l].append(k)
    return graf


def dfs(lacznik, graf, chodnik):
    if chodnik and lacznik == 0:
        return chodnik
    
    if lacznik not in graf or len(graf[lacznik]) == 0:
        return None
    
    for k in list(graf[lacznik]):
        graf[lacznik].remove(k)

        wynik = dfs(k[2], graf, chodnik + [k])
        if wynik is not None:
            return wynik
        
        graf[lacznik].append(k)

    return None


def dfs_iterative(graf):
    stack = [(0, [], {k: v.copy() for k,v in graf.items()})]
    while stack:
        lacznik, chodnik, graph = stack.pop()

        if chodnik and lacznik == 0:
            return chodnik
        
        if lacznik not in graph or not graph[lacznik]:
            continue

        for k in list(graph[lacznik]):
            new_graph = { node: edges.copy() for node,edges in graph.items()}
            new_graph[lacznik].remove(k)
            stack.append((k[2], chodnik + [k], new_graph))
    return None
        



print(dfs_iterative(zbuduj_graf(kostki)))
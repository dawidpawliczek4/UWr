

def Trec(n, m):
    if n == 0 and m > 0:
        return m
    if m == 0 and n >= 0:
        return n
    return Trec(n-1, m) + 2 * Trec(n, m-1)


print(Trec(3,4))


def Titer(n, m):
    # Dwie listy do przechowywania aktualnej i poprzedniej linii
    prev_line = [0] * (m + 1)
    current_line = [0] * (m + 1)

    # Inicjalizacja pierwszej linii (przypadki bazowe dla T(0, m))
    for j in range(m + 1):
        prev_line[j] = j

    # Obliczanie kolejnych linii
    for i in range(1, n + 1):
        # Aktualizacja pierwszego elementu w bieżącej linii (przypadki bazowe dla T(n, 0))
        current_line[0] = i
        for j in range(1, m + 1):
            current_line[j] = current_line[j - 1] + 2 * prev_line[j]
        # Aktualizacja linii poprzedniej
        prev_line = current_line[:]
    
    return current_line[m]

print(Titer(3,4))
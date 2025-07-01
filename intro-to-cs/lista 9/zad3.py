def poprawne(a, n):
    for i in range(n):
        for j in range(i+1, n):
            # Sprawdź, czy hetmany nie są w tym samym wierszu
            if a[i] == a[j]:
                return 0

            # Sprawdź, czy hetmany nie są na tych samych przekątnych
            # Hetmany są na tej samej przekątnej, jeśli odległość między ich kolumnami
            # jest równa odległości między ich wierszami
            if abs(a[i] - a[j]) == abs(i - j):
                return 0

    # Jeśli żadne z powyższych warunków nie zostały spełnione, ustawienie jest poprawne
    return 1

def hetmany(n, k, a):
    if k == n:
        return poprawne(a, n)
    for i in range(n):
        a[k] = i
        if hetmany(n, k+1, a):
            return 1
    return 0


n = 8  # ustal rozmiar szachownicy
a = [-1] * n  # inicjalizacja tablicy a wartościami -1, co oznacza brak hetmana w każdej kolumnie
wynik = hetmany(n, 0, a)
print(a)
def sito(n):
    # Utwórz tablicę o długości n+1, początkowo wypełnioną jedynkami.
    # Zerujemy indeks 0 i 1, bo 0 i 1 nie są liczbami pierwszymi.
    s = [1]*(n+1)
    s[0] = s[1] = 0

    p = 2
    while p**2 <= n:
        # Jeśli prime[p] nie zostało zmienione, to jest to liczba pierwsza.
        if s[p] == 1:
            # Wykreślamy wszystkie wielokrotności p
            for i in range(p**2, n+1, p):
                s[i] = 0
        p += 1

    # Zwracamy wszystkie liczby pierwsze (indeksy z wartością 1)
    return s


print(sito(5))
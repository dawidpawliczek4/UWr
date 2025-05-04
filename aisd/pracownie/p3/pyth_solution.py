import sys

def main():
    data = sys.stdin.read().split()
    if not data:
        return
    # Odczyt pierwszego wiersza: n - liczba kolumn, p - liczba wzorców, mod - wartość m
    n = int(data[0])
    p = int(data[1])
    mod = int(data[2])
    
    # Wczytujemy wzorce. Każdy wzorzec ma 3 wiersze, każdy zawierający 3 znaki ('.' lub 'x')
    forbidden_set = set()
    index = 3
    for _ in range(p):
        # Zapisujemy jako krotkę 3 wierszy
        pattern = (data[index], data[index+1], data[index+2])
        forbidden_set.add(pattern)
        index += 3

    # Prekomputacja dozwolonych przejść
    # allowed[mask1][mask2] - lista mask3, dla której układ trzech kolumn (mask1, mask2, mask3)
    # dla każdego z 3 możliwych pionowych przesunięć (wiersze 0-2, 1-3, 2-4) nie zawiera zakazanego wzorca.
    allowed = [[[] for _ in range(32)] for _ in range(32)]
    for mask1 in range(32):
        for mask2 in range(32):
            for mask3 in range(32):
                valid = True
                # Sprawdzamy trzy możliwe pionowe segmenty: od wiersza 0, 1 i 2 (na planszy 5×...)
                for start in range(3):  # start = 0, 1, 2
                    block = []
                    for r in range(start, start + 3):
                        # Dla danej kolumny pobieramy znak: 'x' jeśli dany bit jest ustawiony, '.' w przeciwnym wypadku
                        c1 = 'x' if (mask1 >> r) & 1 else '.'
                        c2 = 'x' if (mask2 >> r) & 1 else '.'
                        c3 = 'x' if (mask3 >> r) & 1 else '.'
                        block.append(c1 + c2 + c3)
                    # Jeżeli taki blok znajduje się w zbiorze zakazanych wzorców, to nie można przejść do mask3
                    if tuple(block) in forbidden_set:
                        valid = False
                        break
                if valid:
                    allowed[mask1][mask2].append(mask3)

    # Inicjalizacja DP:
    # Dla pierwszych dwóch kolumn (n>=3 zgodnie z treścią zadania) wszystkie pary mask są dozwolone,
    # bo nie da się jeszcze utworzyć pełnego bloku 3×3.
    dp = [[1 for _ in range(32)] for _ in range(32)]
    
    # Przechodzimy od kolumny 3 do n
    for col in range(3, n+1):
        # Nowa macierz DP - stan dp dla kolumny col (przy ostatnich dwóch kolumnach)
        new_dp = [[0 for _ in range(32)] for _ in range(32)]
        for mask1 in range(32):
            for mask2 in range(32):
                cnt = dp[mask1][mask2]
                if cnt:
                    # Dla danego stanu (mask1, mask2) rozważamy wszystkie maski mask3,
                    # dla których trzy kolumny (mask1, mask2, mask3) są poprawne.
                    for mask3 in allowed[mask1][mask2]:
                        new_dp[mask2][mask3] = (new_dp[mask2][mask3] + cnt) % mod
        dp = new_dp

    # Wynik to suma po wszystkich stanach dla ostatniej kolumny
    result = sum(dp[mask1][mask2] for mask1 in range(32) for mask2 in range(32)) % mod
    sys.stdout.write(str(result))


if __name__ == '__main__':
    main()

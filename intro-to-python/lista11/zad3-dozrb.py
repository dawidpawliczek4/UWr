def metoda_dhondta(wyniki_komitetow, liczba_mandatow):
    # Przygotowanie listy do przechowywania ilorazów dla każdego komitetu
    ilorazy = []
    for komitet, wynik in wyniki_komitetow.items():
        for i in range(1, liczba_mandatow + 1):
            ilorazy.append((wynik / i, komitet))
    
    # Sortowanie ilorazów malejąco
    ilorazy.sort(reverse=True)

    # Przydzielenie mandatów
    mandaty = {komitet: 0 for komitet in wyniki_komitetow.keys()}
    for i in range(liczba_mandatow):
        _, komitet = ilorazy[i]
        mandaty[komitet] += 1

    return mandaty

# Wyniki wyborów w poszczególnych okręgach
okreg1 = {"Partia A": 40, "Partia B": 30, "Partia C": 20, "Partia D": 10}
okreg2 = {"Partia A": 35, "Partia B": 35, "Partia C": 15, "Partia D": 15}
okreg3 = {"Partia A": 25, "Partia B": 25, "Partia C": 25, "Partia D": 25}

# Obliczanie mandatów w każdym okręgu
mandaty_okreg1 = metoda_dhondta(okreg1, 5)
mandaty_okreg2 = metoda_dhondta(okreg2, 4)
mandaty_okreg3 = metoda_dhondta(okreg3, 3)

print(mandaty_okreg1, mandaty_okreg2, mandaty_okreg3)


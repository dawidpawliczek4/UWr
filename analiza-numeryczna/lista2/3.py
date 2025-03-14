import itertools
import matplotlib.pyplot as plt

# Prosta pętla do wyliczenia wszystkich możliwych kombinacji e_bits i c, aby zobaczyć liczby "ręcznie"
numbers = []

# Iterujemy przez wszystkie kombinacje bitów e_{-2}, e_{-3}, e_{-4}, e_{-5} oraz c
for e2 in [0, 1]:
    for e3 in [0, 1]:
        for e4 in [0, 1]:
            for e5 in [0, 1]:
                for c in [0, 1,-1]:
                    # Mantysa
                    mantissa = 2**-1 + e2 * 2**-2 + e3 * 2**-3 + e4 * 2**-4 + e5 * 2**-5
                    
                    # Uwzględnienie czynnika 2^c
                    exponent = 2**c
                    
                    # Obliczenie wartości dla dodatnich i ujemnych liczb
                    pos_value = mantissa * exponent
                    neg_value = -mantissa * exponent
                    
                    # Dodanie wyników do listy
                    numbers.append(pos_value)
                    numbers.append(neg_value)

# Posortowanie wyników
numbers_manual = sorted(numbers)

# Sprawdzenie maksymalnej wartości
max_value_manual = max(numbers_manual)
max_value_manual

A = min(numbers)
B = max(numbers)

# Wynik
print(f"Przedział [A, B]: [{A}, {B}]")
print("Liczby rozkładają się w przedziale następująco:")
numbers.sort()
print(numbers)

# Rysowanie linii z zaznaczonymi liczbami
plt.figure(figsize=(10, 2))
plt.plot(numbers, [1]*len(numbers), 'ro')  # punkty na linii
plt.yticks([])  # usunięcie osi y, bo nie jest potrzebna
plt.title("Rozkład liczb w przedziale [A, B]")
plt.xlabel("Wartości liczb")
plt.grid(True)

plt.show()
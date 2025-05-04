import numpy as np

data = np.loadtxt('z0801.csv', delimiter=',')

# 2) Oblicz liczbę obserwacji
n = data.size

# 3) Oblicz średnią próby X̄
X_bar = data.mean()

# 4) Oblicz nieobciążoną wariancję próbki S²
S2 = data.var(ddof=1)

# 5) Wyświetl wyniki
print(f"Liczba obserwacji (n): {n}")
print(f"Średnia próby (X̄): {X_bar:.4f}")
print(f"Wariancja próbki (S²): {S2:.4f}")

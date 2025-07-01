import pandas as pd
import numpy as np
from scipy.stats import norm

# Parametry
alpha = 0.05  # Poziom istotności (dla 95% przedziału ufności)

# 1. Wczytanie danych: zakładamy, że l13z05.csv ma trzy kolumny bez nagłówka:
#    - etykieta (np. rok lub wiersz) [opcjonalnie],
#    - liczba gęgawy zwyczajnej (A. anser anser),
#    - liczba gęgawy różowodziobej (A. anser rubirostris).
df = pd.read_csv('./l13z05.csv', header=None, names=['Label', 'Count_AnserAnser', 'Count_AnserRubirostris'])

# 2. Obliczenie sumarycznych liczebności obu podgatunków
total_anser_anser = df['Count_AnserAnser'].sum()
total_anser_rubirostris = df['Count_AnserRubirostris'].sum()
total_population = total_anser_anser + total_anser_rubirostris

# 3. Estymator udziału (proporcji) gęgawy zwyczajnej w populacji gęgawy
p_hat = total_anser_anser / total_population

# 4. Obliczenie przedziału ufności metodą aproksymacji normalnej (Wald)
z = norm.ppf(1 - alpha/2)  # krytyczna wartość z dla danego alpha
print("z_alpha/2", z)
se = np.sqrt(p_hat * (1 - p_hat) / total_population)  # błąd standardowy proporcji

lower = p_hat - z * se
upper = p_hat + z * se
print(lower, upper)

# Zamiana na procenty:
lower_pct = lower * 100
upper_pct = upper * 100
p_hat_pct = p_hat * 100

print("Łączna liczebność A. anser anser:", total_anser_anser)
print("Łączna liczebność A. anser rubirostris:", total_anser_rubirostris)
print("Łączna populacja gęgawy:", total_population)
print(f"Estymowana wartość udziału G. zwyczajnej: {p_hat_pct:.2f}%")
print(f"{100*(1-alpha):.1f}% przedział ufności dla udziału: [{lower_pct:.2f}%, {upper_pct:.2f}%]")

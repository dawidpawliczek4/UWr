import pandas as pd
import numpy as np
from scipy.stats import chi2

# Wczytanie danych z pliku CSV
df = pd.read_csv('./l13z01.csv', header=None)

# Suma obserwacji dla każdej z czterech lokalizacji
observed_sum = df.sum(axis=0).values

# Obliczenia statystyki chi-kwadrat
total_count = observed_sum.sum()
expected = np.full_like(observed_sum, total_count / len(observed_sum), dtype=float)
chi2_stat = ((observed_sum - expected) ** 2 / expected).sum()
dfree = len(observed_sum) - 1
p_value = chi2.sf(chi2_stat, dfree)

"""
Hipoteza zerowa- oczekiwana liczba ptakow w akzej lok = laczna liczba / liczba lokalizacji
w chikwadracie sprawdzamy, czy roznice pomiedzy obserwacjami a oczekiwanymi sa okej

chikwadrat = suma po i=1,..,k (Obserwacje_i - Expected_i)^2 / expected_i
"""

# Przygotowanie tabeli wynikowej
results_df = pd.DataFrame({
    'Lokalizacja': [f'L{i+1}' for i in range(len(observed_sum))],
    'Suma obserwowanych': observed_sum,
    'Oczekiwane (przy H₀)': expected,
    'Wkład do χ²': ((observed_sum - expected) ** 2 / expected)
})

print(results_df)

# p_value = 1 - CDF
print(chi2_stat, dfree, p_value)
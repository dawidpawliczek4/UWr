import pandas as pd
from scipy import stats

# 1. Wczytanie danych
# Zakładamy, że plik ma cztery kolumny: 
#   - pierwszy wiersz to etykieta (np. "r1", "r2" itd.),
#   - druga kolumna to liczba Gęgawy zwyczajnej (A. anser anser),
#   - trzecia kolumna to liczba Gęgawy różowodziobej (A. anser rubirostris).
df = pd.read_csv('./l13z05.csv', header=None, names=['Year', 'Count_Aanser', 'Count_Arubirostris'])

alpha = 0.05  # Poziom istotności

print("Wyniki testu goodness-of-fit dla proporcji 2:1 (p1 = 2/3, p2 = 1/3):\n")

# 2. Pętla po każdym wierszu
for idx, row in df.iterrows():
    label = row['Year']
    o1 = row['Count_Aanser']         # obserwowana liczba A. anser anser
    o2 = row['Count_Arubirostris']   # obserwowana liczba A. anser rubirostris
    total = o1 + o2

    # 3. Wyliczenie oczekiwanych wartości przy H0 (2:1)
    e1 = total * (2/3)
    e2 = total * (1/3)

    # 4. Obliczenie statystyki chi-kwadrat
    chisq = (o1 - e1)**2 / e1 + (o2 - e2)**2 / e2

    # 5. Obliczenie p-value (df = 1)
    p_value = 1 - stats.chi2.cdf(chisq, df=1)

    # 6. Decyzja testowa
    decision = "Odrzucamy H0" if p_value < alpha else "Nie odrzucamy H0"

    # 7. Wypisanie wyników dla danego roku
    print(f"{label}: "
          f"O = [{o1}, {o2}], "
          f"E = [{e1:.2f}, {e2:.2f}], "
          f"χ² = {chisq:.3f}, "
          f"p = {p_value:.4f} → {decision}")

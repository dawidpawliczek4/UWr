import pandas as pd        # wygodne wczytywanie CSV
import math
from scipy.stats import norm, t   # dystrybuanty Φ i t-Studenta

CSV_PATH   = "z89.csv"   # ← ścieżka do pliku z danymi
MU_0       = 2.0         # hipoteza H0: μ = 2
SIGMA_KNWN = 3.5         # znane σ (tylko dla zad. 8)

data = pd.read_csv(CSV_PATH, header=None)[0]
n = len(data)            # liczba obserwacji

x_bar = data.mean()      # średnia z próby
S = data.std(ddof=1)     # nieobciążone odchylenie standardowe (ddof=1 ⇒ n-1)

# --- 5. Zadanie 8 → statystyka Z --------------------------------------------
#  Wzór: Z = √n · (x̄ – μ₀) / σ        (σ znane)
z_stat = math.sqrt(n) * (x_bar - MU_0) / SIGMA_KNWN
F_Z    = norm.cdf(z_stat)     # Φ(z) – prawdopodobieństwo P(Z ≤ z)

# --- 6. Zadanie 9 → statystyka T --------------------------------------------
#  Wzór: T = √(n-1) · (x̄ – μ₀) / S    (σ nieznane ⇒ S z próby)
t_stat = math.sqrt(n - 1) * (x_bar - MU_0) / S
df     = n - 1                 # stopnie swobody
F_T    = t.cdf(t_stat, df)     # F_T(t) – P(T ≤ t)

print(f"Liczba obserwacji n      : {n}")
print(f"Średnia próby  x̄        : {x_bar:.6f}")
print(f"Odchylenie próby  S      : {S:.6f}\n")

print("=== Zadanie 8 — statystyka Z (σ znane) ===")
print(f"Z = √n·(x̄ – μ₀)/σ       = {z_stat:.4f}")
print(f"Φ(z) = P(Z ≤ z)         = {F_Z:.6f}\n")

print("=== Zadanie 9 — statystyka T (σ nieznane) ===")
print(f"T = √(n-1)·(x̄ – μ₀)/S   = {t_stat:.4f}   (df = {df})")
print(f"F_T(t) = P(T ≤ t)       = {F_T:.6f}")

import numpy as np
from scipy.stats import t

# 1) Wczytanie danych
data = np.loadtxt('z0801.csv', delimiter=',')
n = data.size
X_bar = data.mean()
S = data.std(ddof=1)   # odchylenie standardowe próbki

# 2) Dla każdej hipotezy obliczamy t-stat (statystyka) i jego CDF
for mu0 in [1.5, 1.75]:
    t_stat = (X_bar - mu0) / (S / np.sqrt(n))
    cdf_value = t.cdf(t_stat, df=n-1)
    print(f"H0: μ = {mu0:<5}  →  t = {t_stat: .4f},  Fₜ(t;49) = {cdf_value: .4f}")

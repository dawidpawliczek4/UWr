import numpy as np
import pandas as pd
from scipy import stats

# 1. Wczytanie danych
data = pd.read_csv('z0104.csv', header=None).iloc[:, 0].values

# Parametry wspólne
mu0 = 3.9
sigma = 1
sample_sizes = [10, 20, 40]

# ----- Zadanie 1: σ znane, statystyka Z -----
print("Zadanie 1 (σ = 1, H0: μ = 3.9):")
print("{:>2s}  {:>10s}  {:>12s}".format("n", "z_stat", "F_Z(z)"))
for n in sample_sizes:
    sample = data[:n]
    mean_n = sample.mean()
    z_stat = (mean_n - mu0) / (sigma / np.sqrt(n))
    z_cdf = stats.norm.cdf(z_stat)
    print(f"{n:2d}  {z_stat:10.4f}  {z_cdf:12.4f}")

# ----- Zadanie 2: σ nieznane, statystyka t -----
print("\nZadanie 2 (σ nieznane, H0: μ = 3.9):")
print("{:>2s}  {:>10s}  {:>12s}".format("n", "t_stat", "F_T(t)"))
for n in sample_sizes:
    sample = data[:n]
    mean_n = sample.mean()
    s_n = sample.std(ddof=1)
    t_stat = (mean_n - mu0) / (s_n / np.sqrt(n))
    t_cdf = stats.t.cdf(t_stat, df=n-1)
    print(f"{n:2d}  {t_stat:10.4f}  {t_cdf:12.4f}")

# ----- Zadanie 3: największe μ0 dla n=20 przy σ znanym -----
n3 = 20
sample3 = data[:n3]
mean3 = sample3.mean()
z_q90 = stats.norm.ppf(0.9)   # kwantyl 0.9 rozkładu N(0,1)
mu0_max_z = mean3 - z_q90 / np.sqrt(n3)
print(f"\nZadanie 3 (największe μ0, n=20, σ=1): {mu0_max_z:.2f}")

# ----- Zadanie 4: największe μ0 dla n=10 przy σ nieznanym -----
n4 = 10
sample4 = data[:n4]
mean4 = sample4.mean()
s4 = sample4.std(ddof=1)
t_q90 = stats.t.ppf(0.9, df=n4-1)  # kwantyl 0.9 rozkładu t(n-1)
mu0_max_t = mean4 - t_q90 * (s4 / np.sqrt(n4))
print(f"Zadanie 4 (największe μ0, n=10, σ nieznane): {mu0_max_t:.2f}")

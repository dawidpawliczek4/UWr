import pandas as pd
import numpy as np
from scipy import stats

# 1) Wczytanie danych
# Jeśli Twój plik ma nagłówek, usuń `header=None`
df = pd.read_csv('l12z4.csv', header=None)
x = df.iloc[:,0].values
y = df.iloc[:,1].values

n1, n2 = len(x), len(y)
xbar, ybar = np.mean(x), np.mean(y)
# próba-wariancje (unbiased)
S1_sq = np.var(x, ddof=1)
S2_sq = np.var(y, ddof=1)

print(f"n1={n1}, n2={n2}")
print(f"x̄1={xbar:.4f}, x̄2={ybar:.4f}")
print(f"S1^2={S1_sq:.4f}, S2^2={S2_sq:.4f}")
print()

# 4) Test H0: μ1 = μ2, znamy σ1^2=S1^2, σ2^2=S2^2 → Z-test
sigma1_sq, sigma2_sq = S1_sq, S2_sq
Z = (xbar - ybar) / np.sqrt(sigma1_sq/n1 + sigma2_sq/n2)
p4_one  = 1 - stats.norm.cdf(Z)
print("4) Z-test (known σ):")
print(f"   Z = {Z:.4f}")
print(f"   answer = {p4_one}")
print()

# 5) Test H0: μ1 = μ2, nie znamy σ1^2, σ2^2 → Welch's t-test
t5 = (xbar - ybar) / np.sqrt(S1_sq/n1 + S2_sq/n2) #wartosc testu t welcha z wzoru
df5 = (S1_sq/n1 + S2_sq/n2)**2 / ((S1_sq/n1)**2/(n1-1) + (S2_sq/n2)**2/(n2-1)) # przyblizona ilosc stopni swobody dla chikwadrat
p5_one = 1 - stats.t.cdf(t5, df=df5)
print("5) Welch’s t-test (nieznane σ):")
print(f"   t = {t5:.4f}, df ≈ {df5:.2f}")
print(f"   p-value (one-sided)  = {p5_one}")
print()

# 6) Test H0: σ1 = σ2, zakładamy μ1,μ2 znane i równe średnim próby n, test F n stopni swobody
sigma1_hat = np.var(x, ddof=0)
sigma2_hat = np.var(y, ddof=0)
F6 = sigma1_hat / sigma2_hat
p6_one = 1 - stats.f.cdf(F6, dfn=n1, dfd=n2)
print("6) F-test (μ znane=średnie próby, wariancje z 1/n):")
print(f"   F = {F6:.4f}")
print(f"   p-value (jednostronnie prawe) = {p6_one}")
print()

# 7) Test H0: σ1 = σ2, nie znamy μ1,μ2 → estymujemy ze sredniej z proby, test Fn-1 stopni swobody
F7 = S1_sq / S2_sq
p7_one = 1 - stats.f.cdf(F7, dfn=n1-1, dfd=n2-1)
print("7) F-test (μ nieznane, wariancje z 1/(n-1)):")
print(f"   F = {F7:.4f}")
print(f"   p-value (jednostronnie prawe) = {p7_one}")

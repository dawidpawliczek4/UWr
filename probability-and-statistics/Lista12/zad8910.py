import pandas as pd
import numpy as np
from scipy.stats import norm

df = pd.read_csv('l12z8.csv', header=None)
u = df.iloc[:,0].values

# metoda odwrotnej dystrybunaty
# dystrybuanta U[0,1] to poprostu x na przedziale (0,1)

# 8. Rozkład N(0,1):
#    F^{-1}(u) = Φ^{-1}(u), gdzie Φ to dystrybuanta rozkładu normalnego
x_norm = norm.ppf(u)

# 9. Rozkład Exp(5):
#   u=F(x) = 1 − e^{−5x}  => e^{-5x} = 1 - u =>   x = −(1/5)·ln(1−u)
x_exp5 = -np.log(1 - u) / 5

# 10. Rozkład o gęstości f(x)=x na [0,2]:
#    Najpierw normalizacja: pole trojkotu sumuje sie do 2, dzielimy przez 2 wiec nowa gestosc g(x)=x/2
    # teraz CDF: calka od 0 do x z t/2dt to x^2/4
    # wiec u = x^2 / 4   =>   x = 2sqrt(u)
x_fx = 2 * np.sqrt(u)

# 3) Wypisanie wyników dla elementów 1., 14., 38. (indeksy 0,13,37)
indices = [0, 13, 37]
print(f"{'i':>3} | {'N(0,1)':>8} | {'Exp(5)':>8} | {'f(x)=x':>8}")
print("-"*35)
for i in indices:
    print(f"{i+1:3d} | {x_norm[i]} | {x_exp5[i]:8.4f} | {x_fx[i]:8.4f}")
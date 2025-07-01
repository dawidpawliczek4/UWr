import numpy as np
import math

# 1) Wczytaj dane
data = np.loadtxt('z0801.csv', delimiter=',')
n = data.size
X_bar = data.mean()

# 2) Parametr znany
sigma = 3.0  # bo sigma^2 = 9

# 3) Lista hipotez H0
for mu0 in [1.5, 1.75]:
    #przeksztalcamy Xbar do postaci zmiennej standaryzowanej, tj odejmujemy u i dzielimy przez sigam / sqrt(n)
    z = (X_bar - mu0) / (sigma / math.sqrt(n))
    # dystrybuanta N(0,1)
    Phi = 0.5 * (1 + math.erf(z / math.sqrt(2)))
    print(f"H0: μ = {mu0:<5}  ->  z = {z: .4f}  ,  Φ(z) = {Phi: .4f}")

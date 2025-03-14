import numpy as np
import math

def f(x):
    return 4 * np.cos(x)**2 - 1

target = math.pi / 3

# Lista wartości x zbliżających się do pi/3
x_values = [target - 10**(-i) for i in range(1, 20)] + [target + 10**(-i) for i in range(1, 20)]

# Obliczanie wartości f(x) dla każdej z x_values
results = [(x, f(x)) for x in x_values]

# Wyświetlanie wyników
for x, fx in results:
    print(f"x = {x:.10f}, f(x) = {fx:.10f}")

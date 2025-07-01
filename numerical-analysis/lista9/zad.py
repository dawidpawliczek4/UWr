import numpy as np
import matplotlib.pyplot as plt
from math import comb

# Punkty kontrolne
control_points = np.array([
    [39.5, 10.5],
    [30, 20],
    [6, 6],
    [13, -12],
    [63, -12.5],
    [18.5, 17.5],
    [48, 63],
    [7, 25.5],
    [48.5, 49.5],
    [9, 19.5],
    [48.5, 35.5],
    [59, 32.5],
    [56, 20.5]
])

# Wagi
weights = np.array([1, 2, 3, 2.5, 6, 1.5, 5, 1, 2, 1, 3, 5, 1])

n = len(control_points) - 1  # stopień krzywej
t_values = np.linspace(0, 1, 500)

# Funkcja do obliczania wielomianów Bernsteina
def bernstein(i, n, t):
    return comb(n, i) * (t**i) * ((1 - t)**(n - i))

# Obliczanie punktów na krzywej
curve = []
for t in t_values:
    # Licznik i mianownik wymiernej definicji krzywej
    numerator_x = 0.0
    numerator_y = 0.0
    denominator = 0.0
    
    for i in range(n + 1):
        B = bernstein(i, n, t)
        w = weights[i]
        numerator_x += B * w * control_points[i, 0]
        numerator_y += B * w * control_points[i, 1]
        denominator += B * w
    
    x = numerator_x / denominator
    y = numerator_y / denominator
    curve.append([x, y])

curve = np.array(curve)

# Rysowanie krzywej
plt.figure(figsize=(8,6))
plt.plot(curve[:,0], curve[:,1], 'r-', label='Wymierna krzywa Béziera')
plt.plot(control_points[:,0], control_points[:,1], 'bo--', label='Punkty kontrolne')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)
plt.show()

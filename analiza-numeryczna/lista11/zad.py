import numpy as np
import matplotlib.pyplot as plt

# 1. Wczytujemy dane
data = np.loadtxt("./punkty.txt", delimiter=",")
t = data[:, 0]
y = data[:, 1]

# 2. Definiujemy funkcję f(t)
def f(t):
    return 6.02 * (t + 3.2) * (t - 0.02) * (t + 1.7)

# (a) Rysujemy f(t) oraz dane
t_plot = np.linspace(t.min(), t.max(), 300)
f_plot = f(t_plot)

plt.figure(figsize=(8, 5))
plt.plot(t_plot, f_plot, label='f(t)', color='red')
plt.scatter(t, y, label='dane', s=10)
plt.legend()
plt.title("Funkcja teoretyczna vs dane")
plt.show()

# (b) Wielomian interpolacyjny (UWAGA: bardzo niestabilne!)
#    Python: np.polynomial.Polynomial.fit(t, y, deg=103)
#    Może powodować ostrzeżenia o słabej kondycji.
#    Lepiej unikać wysokiego stopnia w praktyce.

from numpy.polynomial import Polynomial
poly_inter = Polynomial.fit(t, y, deg=100) 
# Następnie można go rysować na siatce:
p_plot = poly_inter(t_plot)

plt.figure(figsize=(8,5))
plt.scatter(t, y, label='dane', s=10)
plt.plot(t_plot, p_plot, label='Interpolacja, deg=103', color='green')
plt.title("Wielomian interpolacyjny")
plt.legend()
plt.show()

# (c) Wielomiany w sensie min. kw. (stopnie 2 do 15)
plt.figure(figsize=(10,6))
plt.scatter(t, y, color='black', s=10, label='dane')

for deg in [2, 3, 4, 5, 10, 15]:
    p_fit = np.polyfit(t, y, deg=deg)  # zwraca współczynniki od najwyższego stopnia
    p_val = np.polyval(p_fit, t_plot)  # wartości wielomianu na siatce
    plt.plot(t_plot, p_val, label=f'LS deg={deg}')

plt.title("Regresja wielomianowa (różne stopnie)")
plt.legend()
plt.show()

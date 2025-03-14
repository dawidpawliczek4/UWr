import numpy as np
import matplotlib.pyplot as plt

# Function definitions
def f(x):
    return x**2 - np.arctan(x + 2)

# Bisection method implementation
def bisection_method(func, a, b, tol):
    if func(a) * func(b) >= 0:
        print("Bisection method fails. The function must change sign in the interval.")
        return None

    while (b - a) / 2 > tol:
        midpoint = (a + b) / 2
        if func(midpoint) == 0:
            return midpoint  # Found exact zero
        elif func(a) * func(midpoint) < 0:
            b = midpoint
        else:
            a = midpoint

    return (a + b) / 2

tolerance = 1e-6

# Finding zeros
zero1 = bisection_method(f, -2.5, 0, tolerance)  # First zero in the interval [a, 0]
zero2 = bisection_method(f, 0, 2.5, tolerance)  # Second zero in the interval [0, b]

# Plotting the functions g(x) = x^2 and h(x) = arctg(x + 2)
x = np.linspace(-10, 10, 1000)
g = x**2
h = np.arctan(x + 2)

plt.figure(figsize=(10, 6))
plt.plot(x, g, label=r"$g(x) = x^2$", color="blue")
plt.plot(x, h, label=r"$h(x) = \arctan(x + 2)$", color="green")
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')
# plt.axvline(zero1, color='red', linestyle='--', label=f"Zero 1: {zero1:.6f}")
# plt.axvline(zero2, color='orange', linestyle='--', label=f"Zero 2: {zero2:.6f}")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Wykresy funkcji g(x) = x^2 i h(x) = arctg(x + 2)")
plt.legend()
plt.grid(True)
plt.show()

print(zero1, zero2)
import numpy as np

def f(x):
    return 6*x**-3 * (np.arcsin(x) - x)

for i in range(1,20):
    print(f(np.float64(10**(-i))))

def f2(x):
    return 6*x**-3 * (x**3 / 6)

print("\n")
for i in range(1,20):
    print(f2(np.float64(10**(-i))))
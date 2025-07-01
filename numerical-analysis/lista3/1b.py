import numpy as np

def f(x):
    return 10**8 * (np.exp(x) - np.exp(2*x))


for i in range(1,20):
    print(f(np.float64(10**(-i))))

def f2(x):
    return -1 * 10**8 * x

print("\n")
for i in range(1,20):
    print(f2(np.float64(10**(-i))))


def f3(x):
    return 10**8 * (-x + 5/2*(x**2))

print("\n")
for i in range(1,20):
    print(f3(np.float64(10**(-i))))
import numpy as np

def f(x):
    return (8096 * ((np.sqrt(x**13 + 4) - 2 )/ x**14) )


print(f(np.float64(0.001)))

def f2(x):
    return 8096/(x*(np.sqrt(x**13 + 4) + 2))

print(f2(np.float64(0.001)))
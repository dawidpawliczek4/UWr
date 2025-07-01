import numpy as np

def f(x):
    return 1/((x**5) + np.sqrt((x**10) + 2024))


for i in range (1,15):
    print(f(np.int64(-(10**i))))

def f2(x):
    if x > 0:
        return 1/((x**5) + np.sqrt((x**10) + 2024))
    else:
        return (x**5 - np.sqrt(x**10 + 2024)) / (-2024)
    
print("\n\n\n")
for i in range (1,15):
    print(f2(np.int64(-(10**i))))
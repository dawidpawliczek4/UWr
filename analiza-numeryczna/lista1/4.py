import numpy as np
import pandas as pd

def y(x):
    if x == 0:
        return 1
    if x == 1:
        return -1/6
    return (35/6)*y(x-1) + y(x-2)

n = np.arange(2, 30)

y_values32 = np.array([y(np.float32(x)) for x in n], dtype=np.float32)

y_values64 = np.array([y(np.float64(x)) for x in n], dtype=np.float64)

# print(y_values32, y_values64)

# create a pandas frame to display the results beeter way

df = pd.DataFrame({'n': n, 'y_values32': y_values32, 'y_values64': y_values64})

print(df)
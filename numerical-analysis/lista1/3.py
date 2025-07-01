import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def f(x):
    return (1518 * ((2 * x) - np.sin(2 * x))) / (x ** 3)

i_values = np.arange(1, 21)
x_values = 10.0 ** (-i_values)

single_precision_results = np.array([f(np.float32(x)) for x in x_values], dtype=np.float32)

double_precision_results = np.array([f(np.float64(x)) for x in x_values], dtype=np.float64)

df = pd.DataFrame({'power': -i_values ,'x': x_values, 'f(x)_values32': single_precision_results, 'f(x)_values64': double_precision_results})

print(df)
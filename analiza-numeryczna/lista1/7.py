import numpy as np
import matplotlib.pyplot as plt
import math
import pandas as pd

def taylor_sin(x, terms=3):
    approximation = 0
    for n in range(terms):
        sign = (-1)**n
        approximation += sign * (x**(2*n + 1)) / math.factorial(2*n + 1)
    return approximation

x_values = np.linspace(0, np.pi, 20)

true_sin = np.sin(x_values)

approx_sin_3_terms = taylor_sin(x_values, terms=3)
approx_sin_5_terms = taylor_sin(x_values, terms=5)

error_df = pd.DataFrame({'x': x_values, 'true_sin': true_sin, 'approx_sin_3_terms': approx_sin_3_terms, 'approx_sin_5_terms': approx_sin_5_terms})

print(error_df)
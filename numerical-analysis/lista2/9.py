import numpy as np
import pandas as pd

# Define the recursive sequence formula
def compute_x_next(x_k, k):
    return 2**k * np.sqrt(2 * (1 - np.sqrt(1 - (x_k / 2**k)**2)))

# Initial value of the sequence
x1 = np.float64(2)
num_iterations = 40

# Array to hold the computed values
x_values = [x1]

# Compute the sequence for the specified number of iterations
for k in range(1, num_iterations):
    x_next = compute_x_next(x_values[-1], np.float64(k))
    x_values.append(x_next)

df = pd.DataFrame(x_values)

print(df)


x_values = [x1]

def xk_plus_1(x_k, k):
   return (2**k) * (np.sqrt(2 * (
       (((x_k/(2**k))**2)) / (1 + np.sqrt(1-((x_k/(2**k))**2)))
       )))


for k in range(1, num_iterations):
    x_next = xk_plus_1(x_values[-1], np.float64(k))
    x_values.append(x_next)

df = pd.DataFrame(x_values)
print(df)
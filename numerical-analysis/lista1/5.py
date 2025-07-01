import math
import pandas as pd

def calculate_integrals(n_max):

    I_values = [math.log(2025 / 2024)]
    
    for n in range(1, n_max + 1):
        I_n = (1 / n) - 2024 * I_values[n - 1]
        I_values.append(I_n)
    
    return I_values

y = calculate_integrals(20)

df = pd.DataFrame({'I_values': y})

print(df.iloc[1:20:2])

print(df.iloc[2:20:2])

# zauwazmy, ze wyniki po n = 3 zaczynaja rosnac, i na zmiane zmieniac znak, co oznacza, ze wynik nie jest poprawny, poniewaz nasz zwiazek rekurencyjny mowi co innego
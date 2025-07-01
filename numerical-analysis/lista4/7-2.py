def newton_sqrt(m, tolerance=1e-10, max_iterations=100):
    x = 1.0  # Początkowe przybliżenie
    iterations = 0

    while iterations < max_iterations:
        next_x = (x + m / x) / 2
        if abs(next_x - x) < tolerance:
            break
        x = next_x
        iterations += 1

    return x, iterations

def sqrt_a(m, c):
    if c%2 == 1:
        m = m * 2
        c = c - 1
    sqrt_m, iterations = newton_sqrt(m)    
    sqrt_a = sqrt_m * (2 ** (c / 2))
    return sqrt_a, iterations

# Przykładowe wartości m i c
m = 0.75  # Przykład z przedziału [1/2, 1]
c = 2     # Przykładowa wartość całkowita
result, iterations = sqrt_a(m, c)
print(f"wynik = {result}, iteracje = {iterations}")


m = 0.5  # Przykład z przedziału [1/2, 1]
c = 5     # Przykładowa wartość całkowita
result, iterations = sqrt_a(m, c)
print(f"wynik = {result}, iteracje = {iterations}")

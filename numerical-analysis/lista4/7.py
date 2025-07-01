def newton_sqrt(a, tolerance=1e-10, max_iterations=100):
    x = 1.0  # Initial guess
    iterations = 0

    while iterations < max_iterations:
        next_x = (x + a / x) / 2
        if abs(next_x - x) < tolerance:
            break
        x = next_x
        iterations += 1

    return x, iterations

# Test the algorithm with 'a' in the given form
m = 0.75  # Example value in the range [1/2, 1]
c = 2     # Example integer
a = m * (2 ** c)
# a = 0.75 * (2 ** 2) = 3
result, iterations = newton_sqrt(a)
print(f"wynik = {result}, iteracje = {iterations}")

def newton_inverse_sqrt(a, tolerance=1e-6, max_iterations=100):
    x = 0.1
    iterations = 0

    while iterations < max_iterations:
        next_x = x * (3 - a * x * x) * 0.5
        if abs(next_x - x) < tolerance:
            break
        x = next_x
        iterations += 1

    return x, iterations

# Test the algorithm with different values of 'a'
a = 36
result, iterations = newton_inverse_sqrt(a)
print(f"1/sqrt({a}) ≈ {result}, Number of iterations: {iterations}")


# Test the algorithm with different values of 'a'
a = 49
result, iterations = newton_inverse_sqrt(a)
print(f"1/sqrt({a}) ≈ {result}, Number of iterations: {iterations}")


# Test the algorithm with different values of 'a'
a = 121
result, iterations = newton_inverse_sqrt(a)
print(f"1/sqrt({a}) ≈ {result}, Number of iterations: {iterations}")

# Test the algorithm with different values of 'a'
a = 225
result, iterations = newton_inverse_sqrt(a)
print(f"1/sqrt({a}) ≈ {result}, Number of iterations: {iterations}")

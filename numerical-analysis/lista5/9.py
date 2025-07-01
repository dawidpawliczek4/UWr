from mpmath import mp, mpf, diff, sqrt, ln

# Ustawienie precyzji obliczeń (np. 128 miejsc po przecinku)
mp.dps = 256

# Definicja funkcji f(x) oraz jej pochodnych
def f(x):
    return x**3 - 2*x + 2

def f_prime(x):
    return 3*x**2 - 2

def f_double_prime(x):
    return 6*x

# Implementacja jednego kroku metody Olvera
def olver_step(x_n):
    fx = f(x_n)
    fpx = f_prime(x_n)
    fppx = f_double_prime(x_n)
    term1 = fx / fpx
    term2 = (fppx / (2 * fpx**2)) * (fx / fpx)**2
    return x_n - term1 - term2

# Funkcja do eksperymentalnego wyznaczenia rzędu zbieżności
def calculate_convergence_order(x0, true_root, num_iterations=10):
    x_n = mpf(x0)  # Konwersja x0 do formatu dużej precyzji
    errors = []

    # Iteracje metody Olvera
    for i in range(num_iterations):
        error = abs(x_n - true_root)
        errors.append(error)
        print(f"Iteracja {i}: x_n = {x_n}, błąd = {error}")
        x_n = olver_step(x_n)
    
    # Obliczenie rzędu zbieżności na podstawie trzech kolejnych błędów
    orders = []
    for i in range(1, len(errors) - 2):
        e_n = errors[i]
        e_n1 = errors[i+1]
        e_n2 = errors[i+2]
        p = ln(e_n2 / e_n1) / ln(e_n1 / e_n)
        orders.append(p)
        print(f"Przybliżony rząd zbieżności po iteracji {i}: p ≈ {p}")

    return orders

# Przybliżony pierwiastek funkcji f(x) (true_root)
true_root = mpf(1.769292354238631)  # Przybliżenie pierwiastka

# Punkt początkowy i liczba iteracji
x0 = mpf(1.5)
num_iterations = 14

# Uruchomienie analizy
calculate_convergence_order(x0, true_root, num_iterations)

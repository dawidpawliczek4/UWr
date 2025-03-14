def newton_method(f, df, x0, tol=1e-6, max_iter=100):
    """
    f: Funkcja, której szukamy miejsca zerowego
    df: Pochodna funkcji f
    x0: Punkt startowy
    tol: Tolerancja (warunek zakończenia)
    max_iter: Maksymalna liczba iteracji
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        dfx = df(x)
        if abs(fx) < tol:
            print(f"Znaleziono rozwiązanie po {i+1} iteracjach: x = {x}")
            return x
        if dfx == 0:
            print("Pochodna jest zerowa, nie można kontynuować.")
            return None
        x = x - fx / dfx
    print("Przekroczono maksymalną liczbę iteracji.")
    return None

# Przykład użycia
f = lambda x: x**2 - 2  # Szukamy pierwiastka kwadratowego z 2
df = lambda x: 2*x
x0 = 1.0  # Punkt startowy
newton_method(f, df, x0)

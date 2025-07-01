def newton_method_g(f, f_prime, x0, r, tol=1e-6, max_iter=100):    
    x = x0
    for i in range(max_iter):
        print(x)
        fx = f(x)
        f_prime_x = f_prime(x)
        if (fx == 0):
            print(f"Zbieżność osiągnięta po {i+1} iteracjach: x = {x}")
            return x
        
        if f_prime_x == 0:      
            print("err")
            return None

        x_new = x - ((r *fx) / f_prime_x)
        if abs(x_new - x) < tol:
            print(f"Zbieżność osiągnięta po {i+1} iteracjach: x = {x_new}")
            return x_new
        x = x_new

    print(x)
    return None

def f(x):
    return (x-1)**3

def f_prime(x):
    return 3*((x-1)**2)


# Przykład funkcji do testu
def g(x):
    return (x-1)

def g_prime(x):
    return 1

r = 3
x0 = 2.5

root = newton_method_g(f, f_prime, x0, r)

print("Przybliżenie miejsca zerowego:", root)
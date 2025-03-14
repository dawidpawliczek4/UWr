import math

def f(a, b, c):    
    delta = b ** 2 - 4 * a * c
    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    return x1, x2


a = 1
c = 1


print("Dla coraz większych wartości b:")
for i in range(1, 10):
    b = 10 ** i  # coraz większe wartości b
    x1, x2 = f(a, b, c)
    print(f"b = {b}, x1 = {x1}, x2 = {x2}")

print("\nDla coraz bardziej ujemnych wartości b:")
for i in range(1, 10):
    b = -10 ** i  # coraz bardziej ujemne wartości b
    x1, x2 = f(a, b, c)
    print(f"b = {b}, x1 = {x1}, x2 = {x2}")



def f2(a, b, c):
    delta = b ** 2 - 4 * a * c
    if b > 0:
        x1 = (-b - math.sqrt(delta)) / (2 * a)
        x2 = c/(a*x1)
        return x2, x1
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = c/(a*x1)
        return x1,x2
    
print("\n\nDla coraz większych wartości b:")
for i in range(1, 10):
    b = 10 ** i  # coraz większe wartości b
    x1, x2 = f2(a, b, c)
    print(f"b = {b}, x1 = {x1}, x2 = {x2}")

print("\nDla coraz bardziej ujemnych wartości b:")
for i in range(1, 10):
    b = -10 ** i  # coraz bardziej ujemne wartości b
    x1, x2 = f2(a, b, c)
    print(f"b = {b}, x1 = {x1}, x2 = {x2}")
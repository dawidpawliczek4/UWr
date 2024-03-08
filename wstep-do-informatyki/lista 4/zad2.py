
# 1
def gcd(a, b):
    # Oblicza największy wspólny dzielnik (NWD) dwóch liczb za pomocą algorytmu Euklidesa.
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    # Oblicza najmniejszą wspólną wielokrotność (NWW) dwóch liczb.
    return (a * b) // gcd(a, b)


# Przykładowe obliczenia dla liczb 12 i 18

print(lcm(6,10))

# 2

def skrocenie_ulamka(a, b):
    GCD = gcd(a, b)

    a = a // GCD
    b = b // GCD
    return a,b

print(skrocenie_ulamka(100,250))
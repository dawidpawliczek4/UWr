def szybkie_potegowanie_iteracyjne(a, b):
    l = 0 # liczba mnozen
    wynik = 1
    while b > 0:
        if b % 2 == 1:
            wynik *= a
            l += 1
        a *= a
        l += 1
        b = b // 2
    return wynik, l


def szybkie_potegowanie_rekurencyjne(a, b):
    if b == 0:
        return 1, 0
    elif b % 2 == 0:
        wynik, l = szybkie_potegowanie_rekurencyjne(a, b // 2)
        return wynik * wynik, l + 1
    else:
        wynik, l = szybkie_potegowanie_rekurencyjne(a , b // 2)
        return wynik * wynik * a, l + 2
    

print(szybkie_potegowanie_rekurencyjne(2, 16))
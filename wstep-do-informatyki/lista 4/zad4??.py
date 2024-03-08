def znajdz_p_i_dzielniki(n, a_list):
    # Słownik, który przechowa pary (podstawa, wykładnik)
    factors = {}
    
    # Znajdź p i dzielniki n
    for a in a_list:
        p = 0
        # Dopóki n jest podzielne przez a, dziel n przez a i zwiększ p
        while n % a == 0:
            n //= a
            p += 1
        if p > 0:
            factors[a] = p
    
    # Znajdź największe p
    p_max = max(factors.values(), default=0)
    
    # Znajdź liczby a_i, których p-ta potęga jest dzielnikiem n
    dzielniki = [a for a, p in factors.items() if p == p_max]
    
    return p_max, dzielniki

# Przykładowe wywołanie funkcji
n = 63000
a_list = [2, 3, 5]
p, dzielniki = znajdz_p_i_dzielniki(n, a_list)
print(f'Wartość p: {p}')
print(f'Dzielniki: {dzielniki}')

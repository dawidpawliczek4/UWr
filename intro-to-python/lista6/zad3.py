def znajdz_dzielniki_pierwsze(n):
    dzielniki = set()
    
    while n % 2 == 0:
        dzielniki.add(2)
        n //= 2
    
    i = 3
    while i * i <= n:
        while n % i == 0:
            dzielniki.add(i)
            n //= i
        i += 2
    
    if n > 2:
        dzielniki.add(n)

    return dzielniki


print(znajdz_dzielniki_pierwsze(1890427))
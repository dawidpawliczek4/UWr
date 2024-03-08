def podzbiory(s):
    if len(s) == 0:
        return [[]]

    elem = s.pop()
    bez_elem = podzbiory(s)
    z_elem = [podzbior + [elem] for podzbior in bez_elem]

    return bez_elem + z_elem


def suma_ostatnich_cyfr(L):
    return sum(liczba % 10 for liczba in L)


def najwieksza_liczba_z_cyfr(L):    
    return int(''.join(str(liczba) for liczba in sorted(L, reverse=True)))


def najmniejszy_pierwszy_dzielnik(n):
    return min(dzielnik for dzielnik in range(2, n+1) if n % dzielnik == 0)

def pisane_wielka_litera(L):
    [slowo for slowo in L if slowo[0].isupper() and slowo[1:].islower() and len(slowo) > 1]
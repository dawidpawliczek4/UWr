def podzbiory(s):
    if len(s) == 0:
        return [[]]

    elem = s.pop()
    bez_elem = podzbiory(s)
    z_elem = [podzbior + [elem] for podzbior in bez_elem]

    return bez_elem + z_elem

# Przykładowe użycie
s = {1, 2, 3}
wynik = podzbiory(list(s))
print(wynik)

from itertools import permutations

def sprawdz_rozwiazanie(zagadka, przypisanie):
    tabela_translacji = str.maketrans(przypisanie)
    przetlumaczona_zagadka = zagadka.translate(tabela_translacji)
    # print(przetlumaczona_zagadka)

    skladniki, wynik = przetlumaczona_zagadka.split('=')
    skladniki = skladniki.split('+')
    # print(skladniki, wynik)

    try:
        return (all(skladnik[0] != '0' for skladnik in skladniki + [wynik])) and (sum(int(skladnik) for skladnik in skladniki) == int(wynik))
    except ValueError:
        return False

def solve(zagadka):
    unikalne_litery = set(filter(str.isalpha, zagadka))
    
    if len(unikalne_litery) > 10:
        return None

    for perm in permutations('0123456789', len(unikalne_litery)):
        przypisanie = dict(zip(unikalne_litery, perm))        
        # print(przypisanie)
        if sprawdz_rozwiazanie(zagadka, przypisanie):
            return przypisanie

    return None

zagadka = "send + more = money"
print(solve(zagadka))

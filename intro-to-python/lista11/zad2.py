def permutacyjna_postac_normalna(slowo):    
    litera_do_liczby = {}    
    licznik = 1    
    wynikowe_liczby = []
    for litera in slowo:
        if litera not in litera_do_liczby:            
            litera_do_liczby[litera] = licznik
            licznik += 1
        wynikowe_liczby.append(str(litera_do_liczby[litera]))    
    return '-'.join(wynikowe_liczby)


test = ["tak", "nie", "tata", "indianin"]
print([permutacyjna_postac_normalna(slowo) for slowo in test])
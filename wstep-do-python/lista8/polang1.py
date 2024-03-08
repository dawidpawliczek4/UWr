from collections import defaultdict as dd
import random
popularnosc = {}

with open('korpus.txt') as f:
    for line in f:
        linia = line.strip().split()
        for slowo in linia:
            if slowo not in popularnosc:
                popularnosc[slowo] = 1
            else:
                popularnosc[slowo] += 1

# print(popularnosc)

pol_ang = dd(list)

for x in open('pol_ang.txt'):
    x = x.strip()
    L = x.split('=')
    if len(L) != 2:
        continue
        
    pol, ang = L
    pol_ang[pol].append(ang)

def tlumacz(polskie):
    wynik = []
    for p in polskie:
        if p in pol_ang:
            # wynik.append(random.choice(pol_ang[p]))
            popularnosci_tera = {}
            for s in pol_ang[p]:
                if s not in popularnosc:
                    popularnosc[s] = 0                
                else:
                    popularnosci_tera[s] = popularnosc[s]
            print(popularnosci_tera)
            maxval = max(popularnosci_tera.values())
            maxkeys = [ key for key, value in popularnosci_tera.items() if value == maxval]
            print(maxkeys)
            chosen = random.choice(maxkeys)
            wynik.append(chosen)
        else:
            wynik.append('[' + p + ']')
    return wynik        
    
zdanie = 'papuga z wiewiórka pójść do las'.split()

# for i in range(10):
print (' '.join(tlumacz(zdanie)))  
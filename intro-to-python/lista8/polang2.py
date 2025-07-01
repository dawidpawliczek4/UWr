pol_ang = {}

for x in open('pol_ang.txt'):
    x = x.strip()
    L = x.split('=')
    if len(L) != 2:
        continue
        
    pol, ang = L
    pol_ang[pol] = ang

def tlumacz(polskie):
    wynik = []
    for p in polskie:
        if p in pol_ang:
            wynik.append(pol_ang[p])
        else:
            wynik.append('[' + p + ']')
    return wynik        
    
zdanie = 'chłopiec z dziewczyna pójść do kino'.split()

print (' '.join(tlumacz(zdanie)))  
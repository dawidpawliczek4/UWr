def slownik(s):
    slownik = {}
    for l in s:
        if l in slownik:
            slownik[l] += 1
        else:
            slownik[l] = 1
    return slownik

def czyUkladalne(pierwsze, drugie):
    pierwsze = slownik(pierwsze)
    drugie = slownik(drugie)

    for l, c in drugie.items():
        if pierwsze.get(l, 0) < c:
            return False
    return True


f = "lokomotywa"
s = "motyl"
print(czyUkladalne(f, s))  



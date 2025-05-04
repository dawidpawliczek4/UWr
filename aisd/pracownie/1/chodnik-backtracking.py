
n = 0
kostki = []

with open("200k.in") as fin:
    first = True
    for line in fin:
        if first == True:
            n = line.strip()
            first = False
        else:
            kostka = line.strip().split()            
            kostki.append((int(kostka[0]), int(kostka[1]), int(kostka[2])))


def znajdz_chodnik_backtrack(kostki, lacznik, chodnik):
    if chodnik and lacznik == 0:
        return chodnik
    
    for i, k in enumerate(kostki):
        if k[0] == lacznik:
            nowy_ch = chodnik + [k]
            nowy_l = k[2]
            pozostale = kostki[:i] + kostki[i+1:]
            wynik = znajdz_chodnik_backtrack(pozostale, nowy_l, nowy_ch)
            if wynik is not None:
                return wynik
            
    return None

print(
    znajdz_chodnik_backtrack(kostki, 0, [])
)
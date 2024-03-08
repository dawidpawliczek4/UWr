with open("popularne_slowa2023.txt", 'r') as plik:
    slowa = [slowo.strip() for slowo in plik]

def ceasar(s, k, mapa_przesuniec):
    return ''.join(mapa_przesuniec.get(litera, litera) for litera in s)

def znajdz_pary_cesarskie(slowa):
    alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
    dlugosc_alfabetu = len(alfabet)
    pary_cesarskie = []
    max_dlugosc = 0
    mapa_przesuniec = {k: {} for k in range(1, 35)}

    for k in mapa_przesuniec:
        przesuniety_alfabet = alfabet[k % dlugosc_alfabetu:] + alfabet[:k % dlugosc_alfabetu]
        mapa_przesuniec[k] = dict(zip(alfabet, przesuniety_alfabet))    

    szyfrowane_slowa = {}

    for slowo in slowa:
        for k in mapa_przesuniec:
            szyfrowane_slowo = ceasar(slowo, k, mapa_przesuniec[k])
            if szyfrowane_slowo not in szyfrowane_slowa and szyfrowane_slowo != slowo:
                szyfrowane_slowa[szyfrowane_slowo] = slowo
    

    for slowo in slowa:
        if slowo in szyfrowane_slowa:
            para = (szyfrowane_slowa[slowo], slowo)
            dlugosc_pary = len(para[0])
            if dlugosc_pary > max_dlugosc:
                pary_cesarskie = [para]
                max_dlugosc = dlugosc_pary
            elif dlugosc_pary == max_dlugosc:
                pary_cesarskie.append(para)

    return pary_cesarskie

print(znajdz_pary_cesarskie(slowa))
def ceasar(s, k):    
    alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"    
    dlugosc_alfabetu = len(alfabet)
    przesuniety_alfabet = alfabet[k % dlugosc_alfabetu:] + alfabet[:k % dlugosc_alfabetu]
    mapa_przesuniec = dict(zip(alfabet, przesuniety_alfabet))
    szyfrogram = ''.join(mapa_przesuniec[litera] if litera in mapa_przesuniec else litera for litera in s)
    return szyfrogram

testowe_slowo = "abc"
klucz = 5
rez = ceasar(testowe_slowo, klucz)
print(rez)
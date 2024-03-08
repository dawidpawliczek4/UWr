

def szachownica(n,k):

    def rysuj_spacje(dlugosc):
        for i in range(dlugosc):
            print(' ', end="")

    def rysuj_hash(dlugosc):
        for i in range(dlugosc):
            print('#', end="")
    
    def rysuj_wiersz(i, kwadrat, bok): # kwadrat - dlugosc boku pojedynczego kwadratu; bok - dlugosc boku szachownicy
        if i % 2 == 0:
            for i in range(bok):
                rysuj_spacje(kwadrat)
                rysuj_hash(kwadrat)
        else:
            for i in range(bok):
                rysuj_hash(kwadrat)
                rysuj_spacje(kwadrat)


    for i in range(n*2):
        for j in range(k):
            rysuj_wiersz(i, k, n)
            print()

szachownica(3, 2)
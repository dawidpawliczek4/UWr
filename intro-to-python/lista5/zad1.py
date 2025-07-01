import statistics

def wylicz_energie(liczba):

    def F(n):
        if n % 2 == 0:
            return n / 2
        else:
            return 3 * n + 1

    def find_next(aktualna):
        return F(aktualna)

    szukaj = True
    pozycja = 0

    while szukaj:
        liczba = find_next(liczba)
        pozycja += 1
        if liczba == 1:
            szukaj = False
    return pozycja

print(wylicz_energie(7))


def analiza_collatza(a,b):
    maksiumum = 0
    minimum = 0
    energie_wszystkie = []
    for i in range(a, b+1):
        energia = wylicz_energie(i)
        energie_wszystkie.append(energia)
        if energia > maksiumum:
            maksiumum = energia
        if energia < minimum:
            minimum = energia
    print("Max: ", maksiumum)
    print("Min: ", minimum)
    srednia = sum(energie_wszystkie) / len(energie_wszystkie)
    print("Srednia arytmetyczna: ", srednia)
    mediana = statistics.median(energie_wszystkie)
    print("Mediana", mediana)

    
analiza_collatza(5,10)

liczby = {

  1 : 'jeden',

  2 : 'dwa',

  3 : 'trzy',

  4 : 'cztery',

  5 : 'pięć',

  6 : 'sześć',

  7 : 'siedem',

  8 : 'osiem',

  9 : 'dziewięć',

  10 : 'dziesięć',

  11 : 'jedenaście',

  12 : 'dwanaście',

  13 : 'trzynaście',

  14 : 'czternaście',

  15 : 'piętnaście',

  16 : 'szesnaście',

  17 : 'siedemnaście',

  18 : 'osiemnaście',

  19 : 'dziewiętnaście',

  20 : 'dwadzieścia',

  30 : 'trzydzieści',

  40 : 'czterdzieści',

  50 : 'pięćdziesiąt',

  60 : 'sześćdziesiąt',

  70 : 'siedemdziesiąt',

  80 : 'osiemdziesiąt',

  90 : 'dziewięćdziesiąt',

  100 : 'sto',

  200 : 'dwieście',

  300 : 'trzysta',

  400 : 'czterysta',

  500 : 'pięćset',

  600 : 'sześćset',

  700 : 'siedemset',

  800 : 'osiemset',

  900 : 'dziewięćset'

}


def tekstowa(n):
    ret = []
    i = 10
    if n%100 < 20 and n%100>10:        
        ret.append(liczby[n%100])
        n = n - n%100
    while n != 0:
        if n%i != 0:
            ret.append(liczby[n%i])
        n = n - n%i
        i *= 10   
    return ' '.join(ret[::-1])

print(tekstowa(10))
print(tekstowa(5))
print(tekstowa(13))
print(tekstowa(20))
print(tekstowa(25))
print(tekstowa(100))
print(tekstowa(117))
print(tekstowa(290))
print(tekstowa(283))

def napis_z_liczbami(l):
    ret = []
    for slowo in l:
        if type(slowo) == int:            
            ret.append(tekstowa(slowo))
        elif slowo.isnumeric():
            slowo = int(slowo)
            ret.append(tekstowa(slowo))
        else:
            ret.append(slowo)
    return ' '.join(ret)

print(napis_z_liczbami(['Ala', 'ma', '123', 'koty', 13]))
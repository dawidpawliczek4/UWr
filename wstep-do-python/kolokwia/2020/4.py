
slownik = {}

with open("grzybiorze.txt") as f:
    for line in f:
        line = line.split()
        imie = line[0]
        wagi = [float(waga) for waga in line[1:]]
        if imie in slownik:
            slownik[imie] += wagi
        else:
            slownik[imie] = wagi

print(slownik)

slownik2 = {}

for imie in slownik:
    slownik2[imie] = sum(slownik[imie])


slownik2 = dict(sorted(slownik2.items(), key=lambda x: x[1], reverse=True))

for imie in slownik2:
    print(imie, slownik2[imie])
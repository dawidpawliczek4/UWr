from zad1 import pierwsza

tabl = []

siodemki = "7777777"

def hiperszczesliwa():
    for i in range(10):
        for j in range(10):
            for k in range(10):
                liczba = ""
                liczba = siodemki + str(i) + str(j) + str(k)
                tabl.append(liczba)
                liczba = str(i) + siodemki + str(j) + str(k)
                tabl.append(liczba)
                liczba = str(i) + str(j) + siodemki + str(k)
                tabl.append(liczba)
                liczba = str(i) + str(j) + str(k) + siodemki
                tabl.append(liczba)

hiperszczesliwa()

ile_hiper = 0

temp = []

for liczba in tabl:
    if pierwsza(int(liczba)) and liczba[0] != '0' and liczba not in temp:
        ile_hiper += 1
        temp.append(liczba)
        print(liczba)

print(ile_hiper)






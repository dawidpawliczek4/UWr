import math

def silnia(n):
    suma = 1
    for i in range(1, n+1):
        suma = suma * i
    return suma


for i in range(4, 101):
    liczba = silnia(i)
    ile = len(str(liczba))
    print(i, "! ma ", ile, "cyfry" if ile%10 <= 4 and ile%10!= 0 and ile%10!=1 and (ile<10 or ile>20) else "cyfr")


# drugi sposob
for i in range(4, 101):
    liczba = silnia(i)
    ile = int(math.log10(liczba)) + 1
    print(i, "! ma ", ile, "cyfry" if ile%10 <= 4 and ile%10!=0 and ile%10!=1 and (ile<10 or ile>20) else "cyfr")


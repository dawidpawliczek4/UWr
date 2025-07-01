import turtle
from duze_cyfry import daj_cyfre
import random



liczba = input()
liczba = [int(i) for i in liczba]

for r in range(5):  
    for i in liczba:
        print(daj_cyfre(i)[r], end=" ")
    print()  

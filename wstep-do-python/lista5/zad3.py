import turtle
from duze_cyfry import daj_cyfre
import random


liczba = input()
liczba = [int(i) for i in liczba]
print(liczba)
tablica = []

for r in range(5):
    linia = ""
    for i in liczba:
        linia += (daj_cyfre(i)[r])
    tablica.append(linia)    

  
temp = random.randint(0,1)
turtle.fillcolor((temp, temp, temp))

dlugosc_kwadracika = 10
wysokosc_kwadracika = 15    

turtle.speed(0)        



for i in range(len(tablica)):
    
    print(tablica[i])
    for kwadracik in tablica[i]:
        if kwadracik == "#":
            turtle.pendown()
            turtle.begin_fill()
        else:
            turtle.penup()
        turtle.forward(dlugosc_kwadracika)
        turtle.left(90)
        turtle.forward(wysokosc_kwadracika)
        turtle.left(90)
        turtle.forward(dlugosc_kwadracika)
        turtle.left(90)
        turtle.forward(wysokosc_kwadracika)
        turtle.left(90)
        turtle.forward(dlugosc_kwadracika)
        turtle.end_fill()
    turtle.penup()
    turtle.goto(0, -(i+1)*wysokosc_kwadracika)
    turtle.pendown()

turtle.end_fill()


turtle.done()
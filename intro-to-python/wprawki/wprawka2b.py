import turtle
import random


turtle.speed(0)
def rysuj_kwadrat(dlugosc, kolor):
    turtle.penup()
    turtle.backward(dlugosc / 2)
    turtle.right(90)
    turtle.forward(dlugosc / 2)
    turtle.left(90)
    turtle.pendown()
    turtle.fillcolor(kolor)
    turtle.begin_fill()
    for i in range(4):        
        turtle.forward(dlugosc)
        turtle.left(90)
    turtle.end_fill()

for i in range(300, 100, -5):
    iledodajemy = (300-i)//3
    x = random.randint(0-iledodajemy, 100+iledodajemy)
    y = random.randint(0-iledodajemy, 100+iledodajemy)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()    
    rysuj_kwadrat(i, (1, (x+iledodajemy)/(100+2*iledodajemy), (y+iledodajemy)/(100+2*iledodajemy)))

for i in range(100, 15, -1):
    iledodajemy = (300-i)//3
    x = random.randint(0-iledodajemy, 100+iledodajemy)
    y = random.randint(0-iledodajemy, 100+iledodajemy)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()    
    rysuj_kwadrat(i, (1, (x+iledodajemy)/(100+2*iledodajemy), (y+iledodajemy)/(100+2*iledodajemy)))


turtle.done()



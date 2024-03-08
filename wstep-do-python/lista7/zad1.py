import turtle

obrazek_txt = []

with open('./obrazek.txt') as f:
    for l in f:
        obrazek_txt.append(l.strip().split(" "))

# turtle.speed(0)
turtle.tracer(0,1)
turtle.colormode(255)

koord = -5

for linia in obrazek_txt:
    for kwadracik in linia:
        kolor = eval(kwadracik)
        turtle.fillcolor(kolor)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(5)
            turtle.left(90)
        turtle.end_fill()
        turtle.forward(5)
    turtle.penup()
    turtle.goto(0, koord)
    turtle.pendown()
    koord -= 5


turtle.done()
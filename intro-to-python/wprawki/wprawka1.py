import turtle
import random

zolw = turtle.Turtle()

zolw.speed(0)

poczatkowe_kreski = 1

kolory = ["red", "yellow", "blue", "violet", "brown", "green", "orange"]

def kwadrat(bok, kreski):
    margines = 5
    for i in range(4):
        zolw.forward(bok)
        zolw.left(90)
    for i in range(kreski):
        zolw.forward(bok//(1+kreski))
        zolw.left(90)
        zolw.penup()
        zolw.forward(margines)
        zolw.pendown()
        zolw.pencolor(random.choice(kolory))
        zolw.forward(bok-2*margines)
        zolw.left(180)
        zolw.forward(bok-2*margines)
        zolw.pencolor("black")
        zolw.penup()
        zolw.forward(margines)
        zolw.left(90)
        zolw.pendown()
    zolw.backward(kreski*(bok//(1+kreski)))
    zolw.penup()
    zolw.forward(50+5)
    zolw.pendown()


for j in range(4):
    for i in range(poczatkowe_kreski, poczatkowe_kreski+4):
        kwadrat(50, i)
    poczatkowe_kreski+=1
    zolw.penup()
    zolw.backward(200+4*5)
    zolw.right(90)
    zolw.forward(5+50)
    zolw.left(90)
    zolw.pendown()



turtle.done()
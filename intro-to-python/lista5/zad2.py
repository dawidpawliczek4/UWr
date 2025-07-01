import turtle
import random

zolw = turtle.Turtle()

zolw.speed(0)

for i in range(15, 100, +3):
    wysokosc = random.randint(i-3, i+3)
    zolw.forward(10)
    zolw.left(90)
    zolw.forward(wysokosc)
    zolw.left(90)
    zolw.forward(10)
    zolw.left(90)
    zolw.forward(wysokosc)
    zolw.left(90)
    zolw.forward(10)
    zolw.penup()
    zolw.forward(3)
    zolw.pendown()





turtle.done()
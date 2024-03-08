import turtle
import math

t = turtle.Turtle()
t.speed(0)


for i in range(1, 62):
    t.left(90)
    t.forward(math.sin(i/10)*60)
    t.right(90)
    t.forward(7)
    t.right(90)
    t.forward(math.sin(i/10)*60)
    t.left(90)

t.left(180)
t.forward(7*62)

turtle.done()
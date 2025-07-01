import turtle

t = turtle.Turtle()


for i in range(100,10,-10):
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.left(90)
    t.forward(i)
    t.left(90)
    t.penup()
    
    t.forward(10+i/10)
    t.left(90)
    t.forward(10+i/10)
    t.right(90)
    t.pendown()


turtle.done()
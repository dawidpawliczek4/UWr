import turtle

def koch_curve(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(order-1, size/3)
            turtle.left(angle)

turtle.speed(0)

for _ in range(3):
    koch_curve(4, 300)
    turtle.right(120)

turtle.done()
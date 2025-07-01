import turtle
from murek import murek
import random

turtle.tracer(0,1)

def duzyKwadrat():

    string = ""

    for _ in range(4):
        string += '!'
        for _ in range(5):
            string += 'f'
            i = random.randint(1,3)
            if i == 1:
                string+= '!'
            elif i == 2:
                string+= '@'
            elif i == 3:
                string+= '#'
        string += 'l'
        

    return string

murek(duzyKwadrat(), 20)

turtle.done()


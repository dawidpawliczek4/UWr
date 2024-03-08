import turtle
from murek import murek
import random

turtle.tracer(0,1)

def kwadrat_2():

    string = ""
    ile=0

    for i in range(1, 25):
        for j in range(i):
            if i < 4:
                string+= '!'
            elif i < 8:
                string+= '@'
            elif i < 12:
                string+= '#'
            elif i < 16:
                string+= '!'
            elif i < 20:
                string+= '@'
            elif i < 24:
                string += '#'
            else:
                string += '!'
            string += 'f'
        string += 'l'
                        
    return string
            
murek(kwadrat_2(), 5)

turtle.done()
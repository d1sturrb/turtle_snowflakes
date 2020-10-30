
#!/bin/python3

import turtle, time
import random

elsa = turtle.Turtle()
turtle.Screen().bgcolor("white")
colours = ["green", "purple", "red", "tomato"]
elsa.speed(0)

elsa.penup()
elsa.backward(100)
elsa.left(45)
elsa.pendown()
    
    
def branch():
    
    i1 = 0    
    while i1 < 3:
        i2 = 0
        while int2 < 3:
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
        i2 += 1
    elsa.right(90)
    elsa.forward(90)
    i1 += 1
    
i3 = 0
while i3 < 4:
    i4 = 0
    while i4 < 8:
            branch()
            elsa.color(random.choice(colours))
            elsa.left(45)
    i4 += 1

    elsa.penup()
    elsa.forward(250)
    elsa.right(270)
    elsa.pendown()
i3 += 1


time.sleep(3)
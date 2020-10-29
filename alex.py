
#!/bin/python3

# import modules
import turtle, time
import random

# create object "elsa" from class "Turtle" of module turtle
elsa = turtle.Turtle()

turtle.Screen().bgcolor("white")
colours = ["green", "purple", "red", "tomato"]

elsa.speed(0)
elsa.penup()
elsa.backward(100)
elsa.left(45)
elsa.pendown()
    
# new function to create every branch
def branch():
    
    # loop 3 times
    for i in range(3):
        for i in range(3):
            elsa.forward(30)
            elsa.backward(30)
            elsa.right(45)
        elsa.left(90)
        elsa.backward(30)
        elsa.left(45)
    elsa.right(90)
    elsa.forward(90)
    
# loop 4 times
for i in range (4):
    for i in range(8):
           
            branch() # call function "branch()"
            elsa.color(random.choice(colours)) # select random color for turtle
            elsa.left(45)
            

    elsa.penup()
    elsa.forward(250)
    elsa.right(270)
    elsa.pendown()


time.sleep(3) # freeze the windows for 3 seconds before closing

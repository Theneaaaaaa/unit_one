# Thenea Sun
# Sept. 13th
# assignment_one
# This is my first project about how to use turtle for drawing different graphs, I chose to create a beautiful graph
# with repeating hexagon and diamond.

import turtle

turtle.speed(75)

turtle.pencolor('#5DADE2')

turtle.pensize(2)


def make_a_hexagon():
    for x in range(6):
        turtle.forward(150)
        turtle.left(60)


for x in range(20):
    make_a_hexagon()
    turtle.left(18)

turtle.pencolor('#00CCFF')

turtle.pensize(1)


def make_a_diamond():
    for x in range(1):
        turtle.forward(150)
        turtle.left(15)
    for x in range(1):
        turtle.forward(150)
        turtle.left(165)
    for x in range(1):
        turtle.forward(150)
        turtle.left(15)
    for x in range(1):
        turtle.forward(150)
        turtle.left(165)


for x in range(20):
    make_a_diamond()
    turtle.left(18)

turtle.exitonclick()
import turtle

turtle.speed(75)

turtle.pencolor('#5DADE2')

turtle.pensize(2)

def makeAHexagon():
    for x in range(6):
        turtle.forward(150)
        turtle.left(60)


for x in range(20):
    makeAHexagon()
    turtle.left(18)

turtle.pencolor('#00CCFF')

turtle.pensize(1)

def makeADiamond():
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
    makeADiamond()
    turtle.left(18)

turtle.exitonclick()
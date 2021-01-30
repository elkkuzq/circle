import turtle
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def drawCircle(size):
    turtle.pencolor(next(colors))
    turtle.circle(size)
    drawCircle(size + 5)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)

turtle.pencolor('red')
turtle.circle(30)

drawCircle(30)

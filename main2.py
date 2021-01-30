import turtle
from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])

def drawShape(size, angle, shift, shape):
    turtle.bgcolor('black')
    turtle.pencolor(next(colors))
    next_shape= ''
    if shape == 'circle':
        turtle.circle(size)
        next_shape = 'square'
    elif shape == 'square':
        for i in range(4):
            turtle.forward(size * 2)
            turtle.left(90)
        next_shape = 'circle'
    turtle.right(angle)
    turtle.forward(shift)
    drawShape(size + 5, angle + 1, shift + 1, next_shape)

turtle.bgcolor('black')
turtle.speed(100)
turtle.pensize(15)

turtle.pencolor('red')
turtle.circle(30)

drawShape(30, 0, 1, 'circle')

import turtle

side=40
a = 1
turtle.speed('fastest')

for i in range(1,8 * 8 + 1):
    if a % 2 == 1:
        if i % 2 == 1:
            turtle.begin_fill()
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.end_fill()
        turtle.forward(side)
    if a % 2 == 0:
        if i % 2 == 0:
            turtle.begin_fill()
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.forward(side)
        turtle.left(90)
        turtle.end_fill()
        turtle.forward(side)
    if i % 8 == 0:
        turtle.penup()
        turtle.goto(side - 40 ,side * a)
        turtle.pendown()
        a += 1

turtle.exitonclick()
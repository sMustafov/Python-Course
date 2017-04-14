import turtle

turtle.speed('slowest')
length = int(input())
degree = int(input())

while True:
    turtle.forward(length)
    turtle.left(degree)


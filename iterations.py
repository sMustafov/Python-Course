import turtle

g = 134
l = 120
i = 0
stop = int(input())

while True:
    turtle.left(g)
    turtle.forward(l)
    i += 1
    if i == stop:
        break
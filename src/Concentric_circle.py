#circle

import turtle

t = turtle.Turtle()
radius = 10
t.hideturtle()
colors = ["red", "orange", "blue", "green", "yellow"]
for i in range(5):
    print(radius)
    t.pencolor(colors[i])
    t.circle(radius)
    t.penup()
    t.right(90)
    t.forward(10)
    t.left(90)
    radius += 10
    t.pendown()

turtle.done()


# Spiral

import turtle

t = turtle.Turtle()
t.pencolor("blue")
length = 100
for x in range(18):
    t.forward(length)
    t.left(60)
    length -= 5

turtle.done()

# Circles
# import turtle
#
# t = turtle.Turtle()
# radius = 100
# t.hideturtle()
# for i in range(5):
#     t.circle(radius)
#     t.left(90)
#     t.penup()
#     t.forward(radius)
#     t.right(90)
#     t.forward(radius)
#     t.right(90)
#     radius = radius - 20
#     t.forward(radius)
#     t.left(90)
#     t.pendown()
#
# turtle.done()
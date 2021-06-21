import turtle
t = turtle.Turtle()

t.speed(0)


def square():
    for x in range(4):
        t.forward(10)
        t.left(90)


square_count = 3
circle_count = 1

for x in range(4):

    for i in range(square_count):
        square()
        t.penup()
        t.forward(20)
        t.pendown()
        square_count -= 1

    for i in range(circle_count):
        t.penup()
        t.forward(5)
        t.pendown()
        t.circle(5)
        t.penup()
        t.forward(20)
        t.pendown()
        circle_count += 1

turtle.done()

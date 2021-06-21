import turtle
t = turtle.Turtle()

t.speed(0)


def square():
    for x in range(4):
        t.forward(10)
        t.left(90)


for index in range(3):
    square()
    t.penup()
    t.forward(20)
    t.pendown()

for index in range(1):
    t.penup()
    t.forward(5)
    t.pendown()
    t.circle(5)
    t.penup()
    t.forward(20)
    t.pendown()

for index in range(2):
    square()
    t.penup()
    t.forward(20)
    t.pendown()

for d in range(2):
    t.penup()
    t.forward(5)
    t.pendown()
    t.circle(5)
    t.penup()
    t.forward(20)
    t.pendown()

for index in range(1):
    square()
    t.penup()
    t.forward(20)
    t.pendown()

for n  in range(3):
    t.penup()
    t.forward(5)
    t.pendown()
    t.circle(5)
    t.penup()
    t.forward(20)
    t.pendown()

turtle.done()

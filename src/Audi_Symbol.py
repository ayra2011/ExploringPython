import turtle

t = turtle.Turtle()

radius = 50

for x in range(4):
    t.circle(radius)
    t.penup()
    t.forward(radius)
    t.pendown()


turtle.done()

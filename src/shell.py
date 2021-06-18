import turtle

t = turtle.Turtle()
radius = 10
length = 100
distance = 10
t.pendown()
for x in range(5):
    t.circle(radius)
    radius = radius + 10

turtle.done()
t.forward(length)
t.penup()
t.goto(0, distance)
t.pendown()
distance += 10


turtle.done()

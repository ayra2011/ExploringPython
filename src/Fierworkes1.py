import turtle
import random

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(100000)
colors = ['white', 'pink', 'blue', 'purple']

for x in range(50):
    z = random.randint(-450, 450)
    y = random.randint(-450, 450)
    t.penup()
    t.goto(z, y)
    t.pendown()
    size = random.randint(10, 200)

    t.color(random.choice(colors))

    for f in range(36):
        t.forward(size)
        t.backward(size)
        t.right(10)

turtle.done()

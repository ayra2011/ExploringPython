import random
import turtle

t = turtle.Turtle()
screen = turtle.Screen()
screen.bgcolor('black')
t.speed(100000)
colors = ['white', 'pink', 'blue', 'purple']
random_fireworks_num = random.randint(40, 50)

for x in range(random_fireworks_num):
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

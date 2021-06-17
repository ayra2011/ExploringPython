import turtle
from random import randint

f = turtle.Turtle()
tom = turtle.Turtle()
jerry = turtle.Turtle()
tom.shape('turtle')
jerry.shape('turtle')
tom.pensize(5)
jerry.pensize(5)
tom.color('pink')
jerry.color('light blue')
tom.penup()
jerry.penup()
tom.goto(-350, 100)
jerry.goto(-350, -100)
tom.pendown()
jerry.pendown()
f.penup()
f.goto(350, 200)
f.pendown()
f.goto(350, -200)

ts, js = 0, 0

while ts < 700 and js < 700:
    t = randint(10, 40)
    j = randint(10, 40)
    tom.forward(t)
    jerry.forward(j)
    ts += t
    js += j

turtle.done()

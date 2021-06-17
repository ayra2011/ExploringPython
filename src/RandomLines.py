import turtle
import random

t = turtle.Turtle()
tur = turtle.Turtle()

turtle.bgcolor('black')
length = 5000000
currentLength = 0
colours = ['white']
color = 0
t.speed(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
tur.speed(9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)

while currentLength < length:
    t.color(colours[color])
    tur.color(colours[color])
    color = (color + 1) % len(colours)
    lengths = random.randint(5, 50)
    angle = random.randint(5, 90)
    t.bk(lengths)
    tur.fd(lengths)
    t.rt(angle)
    tur.lt(angle)
    currentLength += lengths

turtle.done()

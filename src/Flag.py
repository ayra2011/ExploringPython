import turtle
from tkinter import PhotoImage
from turtle import Turtle, Screen, Shape

screen = Screen()

# substitute 'subsample' for 'zoom' if you want to go smaller:
larger = PhotoImage(file="../tenor.gif").zoom(5, 2)

screen.addshape("larger", Shape("image", larger))

tortoise = Turtle("larger")

tortoise.stamp()

tortoise.hideturtle()

t = turtle.Turtle()
# stair
num = 100
for x in range(3):
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(num)
    num += 100
# flagpole
t.left(90)
t.forward(330)
# outer flag rectangle
for x in range(2):
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(150)
t.backward(50)
# flag lines
t.right(90)
t.forward(200)
# first line
t.left(90)
t.backward(50)
t.left(90)
t.forward(200)
# second line
t.right(90)
t.forward(100)
t.right(90)
# circle
t.forward(80)
t.penup()
t.right(90)
t.forward(75)
t.pendown()
t.circle(25)
t.penup()
t.left(90)
t.forward(25)
t.pendown()
# add spokes to the circle
spokes = 24
for f in range(spokes):
    t.forward(25)
    t.backward(25)
    t.right(360/spokes)
# hide turtle
t.ht()
turtle.done()

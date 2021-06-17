# Assignment 1 - Letter E
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
distance = 0

for x in range(2):
    t.forward(50)
    distance -= 50
    t.backward(50)
    t.goto(0, distance)

t.forward(50)
turtle.done()
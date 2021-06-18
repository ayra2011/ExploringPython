import turtle

t = turtle.Turtle()
turtle.bgcolor('black')
t.pensize(2)
t.speed(999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)

for index in range(6):
    for colour in ['red', 'magenta', 'blue', 'cyan', 'green', 'yellow', 'white']:
        t.color(colour)
        t.circle(100)
        t.lt(10)

t.hideturtle()
turtle.done()

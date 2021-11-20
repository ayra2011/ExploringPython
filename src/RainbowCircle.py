import turtle

t = turtle.Turtle()
totCircleCnt = int(input('enter no. fo circles: '))
t.speed(0)
colours = ['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'indigo']
radius = 7def
t.pensize(15)
for index in range(totCircleCnt):
    t.color(colours[index % 7])
    t.circle(radius)
    radius += 10
    t.penup()
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()
turtle.done()

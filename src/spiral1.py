import turtle

t = turtle.Turtle()

t.color('gold')
t.shape('turtle')
t.speed(1000)
length = 100

for x in range(18):
    t.forward(length)
    t. left(60)
    length = length - 5

t.hideturtle()
turtle.done()
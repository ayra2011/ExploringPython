import turtle
import random

pen = turtle.Turtle()
ball = turtle.Turtle()

ball.shape("circle")
times = random.randint(5,100)

for index in range(times):
    ball.speed(random.randint(0, 10))
    random_angle = random.randint(0, 360)
    ball.right(90)
    random_forward = random.randint(0, 300)
    # ball.forward(random_forward)
    ball.forward(390)
    if ball.forward == (125, 130):
        pen.goto(0, 0)
        pen.write("U lost")
        break

turtle.done()
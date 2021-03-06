import turtle
import random
t = turtle.Turtle()

turtle.bgcolor('black')
t.pensize(3)
t.speed(0)
colour_list = ['orange', 'pink', 'purple', 'light blue', 'red', 'magenta', 'cyan', 'yellow', 'violet']


def square():
    for x in range(4):
        t.forward(10)
        t.left(90)


def square_circle_train():
    square_count = 3
    circle_count = 1
    for x in range(3):

        t.begin_fill()
        turtle.fillcolor()
        t.end_fill()

        for i in range(square_count):
            random_colour_index = random.randint(0, 8)
            t.pencolor(colour_list[random_colour_index])
            square()
            t.penup()
            t.forward(20)
            t.pendown()
        square_count -= 1

        for i in range(circle_count):
            random_colour_index = random.randint(0, 8)
            t.pencolor(colour_list[random_colour_index])
            t.penup()
            t.forward(5)
            t.pendown()
            t.circle(5)
            t.penup()
            t.forward(20)
            t.pendown()
        circle_count += 1


for index in range(8):
    square_circle_train()
    t.penup()
    if (0 == index%2):
        t.right(90)
    else:
        t.left(90)
        # Adjust by 20 to account for reverse bottom
        t.forward(20)
    t.forward(20)
    if (0 == index % 2):
        t.right(90)
    else:
        t.left(90)
    t.forward(13)
    t.pendown()

t.ht()

turtle.done()

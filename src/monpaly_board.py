import platform
import sys
osName = platform.system()
print(osName)

import turtle
t = turtle.Turtle()
screen_mid_to_left = 930
space_between_rectangles = 5


def move_top_left():
    t.setheading(0)
    t.penup()
    t.goto(0, 0)
    t.bk(screen_mid_to_left)
    t.left(90)
    t.fd(493)  # screen_mid_to_top
    t.pendown()


def move_top_right():
    t.setheading(0)
    t.penup()
    t.goto(0, 0)
    t.fd(screen_mid_to_left)
    t.left(90)
    t.fd(493)  # screen_mid_to_top
    t.pendown()


def move_bottom_left():
    t.setheading(0)
    t.penup()
    t.goto(0, 0)
    t.bk(screen_mid_to_left)
    t.right(90)
    t.fd(293)  # screen_mid_to_bottom
    t.pendown()


def rectangle_forward_space(shape_breadth):
    t.setheading(0)
    t.penup()
    t.fd(shape_breadth + space_between_rectangles)
    t.pendown()


def rectangle_downward_space(shape_breadth):
    t.setheading(270)
    t.penup()
    t.fd(shape_breadth + space_between_rectangles)
    t.pendown()


def draw_rectangle(length, breadth):
    t.setheading(0)
    for index in range(2):
        t.forward(length)
        t.right(90)
        t.forward(breadth)
        t.right(90)


def train_horizontal():
    box_horizontal_count = 12
    if "Darwin" == osName:
        box_horizontal_count = 9
    for i in range(box_horizontal_count):
        if i == 0 or i == (box_horizontal_count-1):
            draw_rectangle(rectangle_length, rectangle_length)
            rectangle_forward_space(rectangle_length)
        else:
            draw_rectangle(rectangle_breadth, rectangle_length)
            rectangle_forward_space(rectangle_breadth)


def train_vertical(length, breadth):
    rectangle_downward_space(breadth)  # just for the first box in vertical train we need breadth distance
    for i in range(4):
        draw_rectangle(breadth, length)
        rectangle_downward_space(length)


# Program starts here 😊!!
t.speed(0)
rectangle_length = 200
rectangle_breadth = 140
move_top_left()
train_horizontal()
move_bottom_left()
train_horizontal()
move_top_left()
train_vertical(rectangle_breadth, rectangle_length)
move_top_right()

# to bring turtle from top right to one box left - helps bring right vertical train into screen
t.setheading(0)
t.penup()
t.bk(rectangle_length + space_between_rectangles)
t.pendown()

# right vertical train
train_vertical(rectangle_breadth, rectangle_length)
t.ht()


turtle.done()

import turtle
import tkinter

# screen_width, screen_height = turtle.screensize()
# print("orig: ", screen_height, screen_width)
t = turtle.Turtle()

# make full screen by default
drawing_area = turtle.Screen()
drawing_area.setup(width=.999, height=.999)
# screen_width, screen_height = drawing_area.screensize()
# print("post screen.setup: ", screen_height, screen_width)

# tkinter screen crete , read actual screen size, destroy (we could not find a good way of doing this with turtle - yet)
root = tkinter.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.destroy()
print("actual monitor size: ", screen_height, screen_width)


buffer_from_edge_left_or_right = 20
screen_mid_to_left_or_right = (screen_width / 2) - buffer_from_edge_left_or_right  # 930

buffer_from_edge_top_or_bottom = 80
screen_mid_to_top_or_bottom = (screen_height / 2) - buffer_from_edge_top_or_bottom  # 493 (540 - 60 = 480)

space_between_rectangles = 3

# we know available screen area to draw the monopoly horizontal and vertical trains:
# horizontal screen space : screen_mid_to_left_or_right * 2
# vertical screen space : screen_mid_to_top_or_bottom *  2
# use above information to fit the board :
# - 10 horizontal rectangles each on top and bottom edge of available apace
# - 6 vertical rectangles each on left and right edge of available apace
rectangle_length = 200
rectangle_breadth = 140

box_horizontal_count = 10
box_vertical_count = 6


def move_top_left():
    t.setheading(0)
    t.penup()
    t.goto(0, 0)
    t.bk(screen_mid_to_left_or_right)
    t.left(90)
    t.fd(screen_mid_to_top_or_bottom)
    t.pendown()


def move_top_right():
    t.setheading(0)
    t.penup()
    t.goto(0, 0)
    t.fd(screen_mid_to_left_or_right)
    t.left(90)
    t.fd(screen_mid_to_top_or_bottom)
    t.pendown()


def move_bottom_left():
    t.setheading(0)
    t.penup()
    t.goto(0, 0)
    t.bk(screen_mid_to_left_or_right)
    t.right(90)
    t.fd(screen_mid_to_top_or_bottom)  # old value: 293 (310 after accounting for the up move of 200 - square side)
    t.pendown()


def move_bottom_left_minus_square_side(square_side):
    move_bottom_left()
    t.penup()
    t.bk(square_side)  # old value: 293 (310 after accounting for the up move of 200 - square side)
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
    for i in range(box_horizontal_count):
        if i == 0 or i == (box_horizontal_count-1):
            draw_rectangle(rectangle_length, rectangle_length)
            rectangle_forward_space(rectangle_length)
        else:
            draw_rectangle(rectangle_breadth, rectangle_length)
            rectangle_forward_space(rectangle_breadth)


def train_vertical(length, breadth):
    rectangle_downward_space(breadth)  # just for the first box in vertical train we need breadth distance
    for i in range(box_vertical_count):
        draw_rectangle(breadth, length)
        rectangle_downward_space(length)


# Program starts here 😊!!
t.speed(0)
move_top_left()
train_horizontal()
move_bottom_left_minus_square_side(rectangle_length)
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

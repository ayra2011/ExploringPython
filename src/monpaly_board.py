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
screen_breath = root.winfo_screenwidth()
screen_length = root.winfo_screenheight()
root.destroy()
print("actual monitor size: ", screen_length, screen_breath)


buffer_from_edge_left_or_right = 20
screen_mid_to_left_or_right = (screen_breath / 2) - buffer_from_edge_left_or_right  # 930

buffer_from_edge_top_or_bottom = 80
screen_mid_to_top_or_bottom = (screen_length / 2) - buffer_from_edge_top_or_bottom  # 493 (540 - 60 = 480)

reminder_buffer_from_edge_on_right = 0

space_between_rectangles = 3

# we know available screen area to draw the monopoly horizontal and vertical trains:
# horizontal screen space : screen_mid_to_left_or_right * 2
# vertical screen space : screen_mid_to_top_or_bottom *  2
# use above information to fit the board :
# - 10 horizontal rectangles each on top and bottom edge of available apace
# - 6 vertical rectangles each on left and right edge of available apace
rectangle_length = 0
rectangle_breadth = 0

# includs squares
box_horizontal_count = 0
# excludes squares
box_vertical_count = 5


def compute_rectangle_breadth_and_length():
    square_adjusted_rectangle_count = box_vertical_count + 4  # 2 squares , each double the size of rectangle
    space_between_rectangle_count = box_vertical_count + 1  # squares on both edges of rectangle train
    rectangle_breadth_reserved_for_space = space_between_rectangle_count * space_between_rectangles
    buffer_from_edge_top_plus_bottom = buffer_from_edge_top_or_bottom * 2
    remaining_length = screen_length - buffer_from_edge_top_plus_bottom - rectangle_breadth_reserved_for_space
    global rectangle_breadth, rectangle_length
    rectangle_breadth = remaining_length / square_adjusted_rectangle_count
    rectangle_length = rectangle_breadth * 2


def compute_box_vertical_count():
    space_plus_rectangle_width = rectangle_breadth + space_between_rectangles
    global box_horizontal_count
    buffer_left_plus_right = buffer_from_edge_left_or_right * 2
    # - 2 as squares on both edges of train are double size
    box_horizontal_count = int(((screen_breath-buffer_left_plus_right) / space_plus_rectangle_width)) - 2
    global reminder_buffer_from_edge_on_right
    reminder_buffer_from_edge_on_right = ((screen_breath-buffer_left_plus_right) % space_plus_rectangle_width) + 2 * space_between_rectangles


def compute_variables():
    compute_rectangle_breadth_and_length()
    compute_box_vertical_count()


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
    t.fd(screen_mid_to_left_or_right - reminder_buffer_from_edge_on_right)
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
compute_variables()
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

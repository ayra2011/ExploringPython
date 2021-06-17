import turtle
import random

total_line_length = 0
t = turtle.Turtle()

while 5000 > total_line_length:
    random_line_length = random.randint(1, 100)
    random_angle = random.randint(1, 360)
    t.left(random_angle)
    t.forward(random_line_length)
    print(random_angle)
    total_line_length += random_line_length
    
t.ht()

turtle.done()
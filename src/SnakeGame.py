import turtle
import time
import random

delay = 0.1

# Score
score = 0
high_score = 0

# background colour and shape
window = turtle.Screen()
window.bgcolor('black')
window.setup(width=600, height=600)
window.tracer(0)  # Turns off screen updates

# Snake head
head = turtle.Turtle()
head.speed(1)
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# snake food
food = turtle.Turtle()
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)

segments = []

# pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.ht()
pen.goto(0, 260)
pen.write('Score: 0  Highest Score: 0', align='center', font=('Aral', 50, 'italic'))


# Functions
def go_up():
    head.direction = "up"


def go_down():
    head.direction = "down"


def go_left():
    head.direction = "left"


def go_right():
    head.direction = "right"


def move():
    if head.direction == "up":
        y1 = head.ycor()
        head.sety(y1 + 20)

    if head.direction == "down":
        y1 = head.ycor()
        head.sety(y1 - 20)

    if head.direction == "left":
        x1 = head.xcor()
        head.setx(x1 - 20)

    if head.direction == "right":
        x1 = head.xcor()
        head.setx(x1 + 20)


# Keyboard bindings
window.listen()
window.onkeypress(go_up, 'u')
window.onkeypress(go_down, 'd')
window.onkeypress(go_left, 'l')
window.onkeypress(go_right, 'r')

# main loop
while True:
    window.update()
    num = 660
    nums = 200
    # snake meet with wall
    if head.xcor() > num or head.xcor() < -num or head.ycor() > nums or head.ycor() < -nums:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = 'stop'

        # hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 50, "normal"))

    # snake meet food
    if head.distance(food) < 20:
        # move the food to random position
        x = random.randint(-250, 250)
        y = random.randint(-250, 250)
        food.goto(x, y)

        # new segment
        new_segment = turtle.Turtle()
        new_segment.shape('square')
        new_segment.color('grey')
        new_segment.penup()
        segments.append(new_segment)
        # increase score
        score += 10
        if score > high_score:
            high_score = score

        pen.clear()
        pen.write('score: {} high_score: {}'.format(score, high_score), align='center', font=('Aral', 50, 'italic'))

    # move segments
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)
        segments.speed(0)
    # Move segment 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    time.sleep(delay)

window.mainloop()

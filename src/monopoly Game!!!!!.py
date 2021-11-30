# Exercise 1: Draw the following pattern using while loop and lists. 7
# circles, colors = ["violet","indigo","blue","green","yellow","orange","red"]

# Exercise 2: Draw lines of randomly chosen length, each at a random angle
# with the other - stop drawing when the total length of drawn lines reaches
# 5000 pixels. colors = ["violet","indigo","blue","green","yellow","orange","red"]

# Exercise 3: Use For loop on the following list to calculate (a) Sum (b) average (c) maximum (d) minimum of
# the following numbers:[345, 234, 897, 123, 675, 4365, 8876, 23, 59, 88]Hint: you only need one for loop
# and 3 variables


# Exercise 2:
import random
import turtle

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
t = turtle.Turtle()
for index in range(100):
    random_line_length = random.randrange(50, 100)
    random_angel = random.randint(0, 360)
    t.forward(random_line_length)
    t.right(random_angel)

t.ht()

turtle.done()

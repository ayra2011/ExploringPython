
# Asintment 3
import turtle

t = turtle.Turtle()
print('circle polygon or star,')
user_shape = input('enter any shape from above: ')
if user_shape == 'circle':
    radius = int(input('enter radius of circle: '))
    t.circle(radius)
elif user_shape == 'polygon':
    sides = int(input('enter how many sides do you want: '))
    length = int(input('enter the length of the polygon you want: '))
    for x in range(sides):
        t.forward(length)
        t.right(360/sides)
elif user_shape == 'star':
    print('         enter an odd no')
    sides = int(input('enter how many sides do you want: '))
    length = int(input('enter the length of the star you want: '))
    for z in range(sides):
        t.forward(length)
        t.right(180 - 180/sides)



turtle.done()

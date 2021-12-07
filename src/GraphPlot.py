# importing the required module
import matplotlib.pyplot as plt

x = []
y = []
# # x axis values for drawing M
# x = [2, 2, 3, 4, 4]
# #  y axis values for drawing M
# y = [1, 5, 3, 5, 1]

point_count = int(input('Enter num of points (x,y) to plot: '))
for index in range(point_count):
    x.append(int(input('Enter x coordinate: ')))
    y.append(int(input('Enter y coordinate: ')))


# plotting the points
# plot lines
plt.plot(x, y, label="line 1", linestyle=":")
plt.plot(y, x, label="line 2", linestyle="-.")

# naming the x axis
plt.xlabel('x - axis')
# naming the y axis
plt.ylabel('y - axis')

# giving a title to my graph
plt.title('My first graph!')

# function to show the plot
plt.show()


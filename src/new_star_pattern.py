# ****
# ***
# **
# *
num = int(input("How many lines do u want:  "))
line_to_skip = int(input("Which line do u want to skip:  "))

for index in range(num):
    if index != (line_to_skip - 1):
        print("*" * (num - index))

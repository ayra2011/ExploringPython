UserInputHowManyTimesHeOrSheWantProgramToRun = int(input("How many times u want program to run: "))
num1 = 0
num2 = 1
for index in range(UserInputHowManyTimesHeOrSheWantProgramToRun):
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3

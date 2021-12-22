# Write a program to accept user provided names in a list
# print that list
# print again the list - but this time print names that are on indexes aligned with Fibonacci series numbers
numOfTimesMyProgramWillRun = int(input("Enter the number of times the program should run:  "))
userDifiendList = []

for index in range(numOfTimesMyProgramWillRun):
    userDifiendNum = int(input("Enter any number:  "))
    userDifiendList.append(userDifiendNum)

print(userDifiendList)

num1 = 0
num2 = 1

for i in range(numOfTimesMyProgramWillRun):
    print(num1)
    print(num2)
    num3 = num1 + num2
    print(num3)
    num1 = num2
    num2 = num3


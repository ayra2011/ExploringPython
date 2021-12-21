userDefinedList = []
numOfTimesProgramWillRun = int(input("Enter number of times you want program to run:  "))

num = len(userDefinedList) - 1
num1 = numOfTimesProgramWillRun // 2
for index in range(numOfTimesProgramWillRun):
    numInList = int(input("Enter number you want the list to have:  "))
    userDefinedList.append(numInList)


for i in range(num1):
    numInList = userDefinedList[num]
    num -= 2
    userDefinedList.append(numInList)

print(userDefinedList)

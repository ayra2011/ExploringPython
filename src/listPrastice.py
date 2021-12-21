userDefinedList = []
userDefinedListRevers = []
numOfTimesProgramWillRun = int(input("Enter number of times you want program to run:  "))
for index in range(numOfTimesProgramWillRun):
    numInList = int(input("Enter number you want the list to have:  "))
    userDefinedList.append(numInList)

num = len(userDefinedList) - 1
num1 = numOfTimesProgramWillRun // 2

for i in range(num1):
    numInListRevers = userDefinedList[num]
    num -= 2
    userDefinedListRevers.append(numInListRevers)

print(userDefinedList)
print(userDefinedListRevers)

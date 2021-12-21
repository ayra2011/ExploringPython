userDefinedList = []
userDefinedListRevers = []
numOfTimesProgramWillRun = int(input("Enter number of times you want program to run:  "))
for index in range(numOfTimesProgramWillRun):
    numInList = int(input("Enter number you want the list to have:  "))
    userDefinedList.append(numInList)

num = 0
if numOfTimesProgramWillRun % 2 >= 1:
    for i in range(numOfTimesProgramWillRun // 2 + 1):
        numInListRevers = userDefinedList[num]
        num += 2
        userDefinedListRevers.append(numInListRevers)
else:
    for i in range(numOfTimesProgramWillRun // 2):
        numInListRevers = userDefinedList[num]
        num += 2
        userDefinedListRevers.append(numInListRevers)

print(userDefinedList)
print(userDefinedListRevers)

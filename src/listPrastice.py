userDefinedList = []
userDefinedListRevers = []
numOfTimesProgramWillRun = int(input("Enter number of times you want program to run:  "))
for index in range(numOfTimesProgramWillRun):
    numInList = int(input("Enter number you want the list to have:  "))
    userDefinedList.append(numInList)

num = 0
if numOfTimesProgramWillRun % 2 >= 1:
    timesToLoop = numOfTimesProgramWillRun // 2 + 1
    for i in range(timesToLoop):
        numInListRevers = userDefinedList[num]
        num += 2
        userDefinedListRevers.append(numInListRevers)
else:
    timesToLoop = numOfTimesProgramWillRun // 2
    for i in range(timesToLoop):
        numInListRevers = userDefinedList[num]
        num += 2
        userDefinedListRevers.append(numInListRevers)

print(userDefinedList)
print(userDefinedListRevers)

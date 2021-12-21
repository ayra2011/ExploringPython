userDefinedList = []
numOfTimesProgramWillRun = int(input("Enter number of times you want program to run:  "))
for index in range(numOfTimesProgramWillRun):
    numInList = int(input("Enter number you want the list to have:  "))
    userDefinedList.append(numInList)

print(userDefinedList.reverse())

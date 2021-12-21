def BinarySearchInList(list_of_names, name_to_find):
    if not friendNames:
        print("No name in list Ya really need to get friends")
    else:
        returnIsPresentInList = False
        list_of_names.sort()
        if len(list_of_names) > 1:
            while len(list_of_names) > 1:
                middle_index = len(list_of_names) // 2
                if list_of_names[middle_index] <= name_to_find:
                    for name in list_of_names[:middle_index]:
                        list_of_names.remove(name)
                else:
                    for name in list_of_names[middle_index:]:
                        list_of_names.remove(name)
        if list_of_names[0] == name_to_find:
            returnIsPresentInList = True
        return returnIsPresentInList


friendNames = []
enterFriendName = input("Enter name of friend: ")
isPresentInList = BinarySearchInList(friendNames, enterFriendName)
if isPresentInList:
    print("Name you entered is present in tht list")
else:
    print("Name you entered is not present in tht list")

def SearchInList(list_of_names, name_to_find):
    list_of_names.sort()
    print(list_of_names)
    isPresent = False
    for index in range(len(list_of_names)):
        if name_to_find == list_of_names[index]:
            isPresent = True
            break
    return isPresent


def BinarySearchInList(list_of_names, name_to_find):
    list_of_names.sort()
    print(list_of_names)
    print(len(list_of_names))
    for index in range(len(list_of_names) - 1):
        length = len(list_of_names)
        another_variable_for_middle_index = middle_index
        middle_index = length // 2  # double - slash for “floor” division. (//)
        first_half = list_of_names[:middle_index]
        second_half = list_of_names[middle_index:]
        if list_of_names[middle_index - 1] <= name_to_find:
            if list_of_names[middle_index] == name_to_find:
                print("Found at", another_variable_for_middle_index + 1)
                break
            list_of_names = second_half
            print(second_half)
        else:
            list_of_names = first_half


friendNames = ["Ayra", "Mauli", "Celeste", "Aahana", "Olivia", "Ava", "Charlotte", "Amelia", "Isabella", "Mia",
               "Joni", "Emilia"]

enterFriendName = input("Enter name of friend: ")
# needToUseOutside = SearchInList(friendNames, enterFriendName)
# if needToUseOutside:
#     print("Name you entered is present in tht list")
# else:
#     print("Name you entered is not present in tht list")
BinarySearchInList(friendNames, enterFriendName)

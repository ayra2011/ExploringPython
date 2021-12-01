# # Exercise 3: Use For loop on the following list to calculate (a) Sum (b) average
# # (c) maximum (d) minimum of the following numbers:
# # [5, 4, 7, 3, 1, 6, 8, 2, 9]
# # Hint: you only need one for loop and 3 variables
#
# num_list = [5, 4, 7, 3, 1, 6, 8, 2, 9]
# num_of_num = len(num_list)
# um_num = 0
# for index in range(num_of_num):
#     um_num += num_list[index]
# average = (um_num / num_of_num)
# print('Sum =', um_num)
# print('Average =', average)

def is_smallest(input_num, num_list):
    print(num_list)
    for num in num_list:
        print(num)

def return_smaller(num_list):
    print(len(num_list))
    if num_list[0] < num_list[1] and num_list[0] < num_list[2] and num_list[0] < num_list[3]:
        print(num_list[0])
        return num_list[0]
    elif num_list[1] < num_list[2] and num_list[1] < num_list[3]:
        print(num_list[1])
        return num_list[1]
    elif num_list[2] < num_list[3]:
        print(num_list[2])
        return num_list[2]
    else:
        print(num_list[3])
        return num_list[3]


user_number_count = int(input('how many numbers you want to input? '))
um_num_list = []
if user_number_count >= 4:
    for index in range(user_number_count):
        um_num_list.append(int(input('Enter num:  ')))
else:
    print("sorry request can't be proceeded as", user_number_count, "is invalid, pls enter number that is > 3")
    user_number_count = int(input('how many numbers you want to input? '))
    for index in range(user_number_count):
        um_num_list.append(int(input('Enter num:  ')))

is_smallest(6, um_num_list)
return_smaller(um_num_list)

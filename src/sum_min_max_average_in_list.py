# # Exercise 3: Use For loop on the following list to calculate (a) Sum (b) average
# # (c) maximum (d) minimum of the following numbers:
# # [5, 4, 7, 3, 1, 6, 8, 2, 9]
# # Hint: you only need one for loop and 3 variables


# num_list = [5, 4, 7, 3, 1, 6, 8, 2, 9]
# num_of_num = len(num_list)
# um_num = 0
# for index in range(num_of_num):
#     um_num += num_list[index]
# average = (um_num / num_of_num)
# print('Sum =', um_num)
# print('Average =', average)


def return_smaller(num_list):
    for i in range(user_number_count):
        if num_list[i] <= um_num_list:
            print(num_list)


user_number_count = int(input('how many numbers you want to input? '))
um_num_list = []

if user_number_count >= 4:
    for index in range(user_number_count):
        um_num_list = (int(input('Enter num:  ')))
else:
    print("sorry request can't be proceeded as", user_number_count, "is invalid, pls enter number that is > 3")
    user_number_count = int(input('how many numbers you want to input? '))
    for index in range(user_number_count):
        um_num_list = (int(input('Enter num:  ')))

return_smaller(um_num_list)

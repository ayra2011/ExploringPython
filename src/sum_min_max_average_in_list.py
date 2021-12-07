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


def find_min(num_list):
    for idx in range(len(num_list)):
        times_to_compare = len(num_list) - 1
        is_smallest = True
        i = idx
        while i < times_to_compare:
            if num_list[idx] <= num_list[i + 1]:
                pass
            else:
                is_smallest = False
                break
            i += 1
        if is_smallest:  # is_smallest == True
            print("the number", (num_list[idx]), "is the smallest in list: ", num_list)
            break
        # else:
        #     print("the number", (num_list[idx]), "is NOT the smallest in list: ", num_list)


user_number_count = int(input('how many numbers you want to input? '))
um_num_list = []

if user_number_count >= 4:
    for index in range(user_number_count):
        um_num_list.append(int(input('Enter num:  ')))
else:
    print("sorry request can't be proceeded as", user_number_count, "is invalid, pls enter number that is > 3")

find_min(um_num_list)

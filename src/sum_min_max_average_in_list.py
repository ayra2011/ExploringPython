# # Exercise 3: Use For loop on the following list to calculate (a) Sum (b) average
# # (c) maximum (d) minimum of the following numbers:
# # [5, 4, 7, 3, 1, 6, 8, 2, 9]
# # Hint: you only need one for loop and 3 variables


def find_sum(num_list):
    list_len = len(num_list)
    sum_of_list = 0
    for idx in range(list_len):
        sum_of_list += num_list[idx]
    print('Sum =', sum_of_list, 'list =', num_list)
    return sum_of_list


def find_average(num_list):
    average = (find_sum(num_list) / len(num_list))
    print('Average =', average)


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
            print("the number", (num_list[idx]), "is the smallest in list", num_list)
            break


def find_max(num_list):
    for idx in range(len(num_list)):
        times_to_compare = len(num_list) - 1
        is_biggest = False
        i = idx
        while i < times_to_compare:
            if num_list[idx] >= num_list[i + 1]:
                pass
            else:
                is_biggest = True
                break
            i += 1
        if not is_biggest:
            print("the number", (num_list[idx]), "is the biggest in list", num_list)
            break


user_number_count = int(input('how many numbers you want to input? '))
um_num_list = []

if user_number_count >= 4:
    for index in range(user_number_count):
        um_num_list.append(int(input('Enter num:  ')))
else:
    print("sorry request can't be proceeded as", user_number_count, "is invalid, pls enter number that is > 3")

find_min(um_num_list)
find_max(um_num_list)
find_sum(um_num_list)
find_average(um_num_list)

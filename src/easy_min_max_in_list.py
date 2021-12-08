numbers_list = []
user_number_count = int(input('how many numbers you want to input? '))
for index in range(user_number_count):
    input_for_num = int(input('Enter a number: '))
    numbers_list.append(input_for_num)
print(min(numbers_list))
print(max(numbers_list))
print(sum(numbers_list))
print(sum(numbers_list)/len(numbers_list))

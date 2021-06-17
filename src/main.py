lines_of_star = int(input('lines of stars u want: '))
for index in range(lines_of_star):
    if index != 1:
        print('***' * (lines_of_star - index))

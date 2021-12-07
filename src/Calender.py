import calendar

months_dict = {'january': '01', 'jan': '01', '01': '01', '1': '01',
               'february': '02', 'feb': '02', '02': '02', '2': '02',
               'march': '03', 'mar': '03', '03': '03', '3': '03',
               'april': '04', 'apr': '04', '04': '04', '4': '04',
               'may': '05', '05': '05', '5': '05',
               'june': '06', 'jun': '06', '06': '06', '6': '06',
               'july': '07', 'jul': '07', '07': '07', '7': '07',
               'august': '08', 'aug': '08', '08': '08', '8': '08',
               'september': '09', 'sep': '09', '09': '09', '9': '09',
               'october': '10', 'oct': '10', '10': '10',
               'november': '11', 'nov': '11', '11': '11',
               'december': '12', 'dec': '12', '12': '12'}

user_input = 'y'
while user_input.lower() == 'y' or user_input.lower() == 'yes':
    user_input = input('DO you want program to run: ')
    month = input('Enter any month: ')
    yyyy = 0
    mm = 0
    if month.lower() in months_dict.keys():
        yyyy = int(input('Enter any year: '))
        mm = int(months_dict[month.lower()])
    else:
        print('sorry', month, 'is not a month!')
        exit(1)
    print(calendar.month(yyyy, mm))

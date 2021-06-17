
print('         Enter A No. That U Think Is A Leap Year')
print('U HAVE 5 tries!!')
count = 0
for x in range(5):
    year = int(input('Enter any year u want: '))
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            print("It's not Leap Year")
        else:
            print("It's Leap Year")
            count += 1
    else:
        print("It's not a leap year")

print('U HAVE', count, 'POINTS !!')
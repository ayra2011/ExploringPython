import random
idList = []
for index in range(50):
    first_name = (input('Enter your first name: '))
    last_name = (input('Enter your last name: '))
    email = first_name[0] + '.' + last_name + '@gmail.com'
    while email in idList:
        num = str(random.randint(0, 50))
        email = first_name[0] + '.' + last_name + num + '@gmail.com'
    idList.append(email)
    print(email)

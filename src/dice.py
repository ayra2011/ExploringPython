import random
digit = int(input('Enter any digit 1 to 6: '))
random = random.randint(1, 6)
if digit == random:
    print('U Won!')
else:
    print('U Lost!')
    print('sorry computer rolled a dif value witch equals to', random)
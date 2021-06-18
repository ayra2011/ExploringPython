print('only enter good or bad!  <-')
user_feeling = input('Hey, How are you today? ')
user_feeling = user_feeling.lower().split(sep = " ")
print(user_feeling)

if user_feeling == 'good':
    print('Great to hear that!')
elif user_feeling == 'bad':
    print("don't worry, things will get better!")
else:
    print('you wrote', user_feeling)
    print("sorry, I don't understand\n"
          "only enter good or bad!  <-\n"
          "rerun the program if you want to retry it!")


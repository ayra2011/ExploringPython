
def SubjectEvaluation(subject):
    #print('math')
    if (25) < subject:
        print("F")
        print("Better luck next time ! ")

    elif (45) < subject:
        print("E")
        print("Better luck next time ! ")

    elif (50) < subject:
        print("E")
        print(" Good luck ! ")

    elif (60) < subject:
        print("c")
        print("You can do better ! ")

    elif (80) < subject:
        print("B")
        print("You can do better ! ")

    else:
        print("A*")
        print("You are a smarty pant ! ")



print("                Enter Your Marks")
math = int(input("Math =  "))
english = int(input("English =  "))
science = int(input("Science =  "))
mother_tongue = int(input("Mother Tongue =  "))
user_marks = math + english + science + mother_tongue
print("Your total marks are", user_marks)

SubjectEvaluation(math)
SubjectEvaluation(science)
SubjectEvaluation(mother_tongue)
SubjectEvaluation(english)

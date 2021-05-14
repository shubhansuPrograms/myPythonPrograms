#count Uppercase Lowercase

def separation(userInput):
    lowerCase = 0
    upperCase = 0
    for i in range(0,len(userInput)):
        if (userInput[i].isalpha() == True):
            if(userInput[i].islower() == True):
                lowerCase = lowerCase + 1
            else:
                upperCase = upperCase + 1
        else:
            pass
    return lowerCase,upperCase



userIn = str(input("Enter Sentence: "))
lCase,uCase = separation(userIn)
print("LOWER CASE: ",lCase,"\nUPPER CASE: ",uCase)
def squareOddNumber(userInputList):
    userInputList = list(set(userInputList))
    userInputList.sort()
    answerList = []
    for i in range(0,len(userInputList)):
        if(userInputList[i]%2!=0):
            answerList.append(str(userInputList[i]**2))
        else:
            pass
    return answerList

def conversion(userInputList):
    for i in range(0,len(userInputList)):
        userInputList[i] = int(userInputList[i])
    return userInputList

userIn = list(str(input("Enter list separated by ,:")).split(","))
userIn = conversion(userIn)
print(" ".join(squareOddNumber(userIn)))
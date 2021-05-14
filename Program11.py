def operation(binaryList):
    answerList = []
    for i in range (0,len(binaryList)):
        temp = binaryList[i]
        decimalValue = 0
        for j in range(0,len(temp)):
            decimalValue = decimalValue + (int(temp[j])*(2**(len(temp)-1-j)))
        if(decimalValue % 5 == 0):
            answerList.append(temp)
        else:
            pass
    return (" ".join(answerList))

userInput = list(str(input("Enter the decimal values separated by comma: ")).split(","))
print(operation(userInput))
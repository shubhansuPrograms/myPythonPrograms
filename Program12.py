#program to calculate number of digits and alphabets
def separtion(userInput):
    digitCount = 0
    alphabetCount = 0
    for i in range(0,len(userInput)):
        if (userInput[i].isnumeric()==True):
            digitCount = digitCount + 1
        elif (userInput[i].isalpha() == True):
            alphabetCount = alphabetCount + 1
        else:
            pass
    return digitCount,alphabetCount


userIn = str(input("Enter sentence: "))
digit,letter = separtion(userIn)
print("DIGITS: ",digit,"\nLETTERS: ",letter)
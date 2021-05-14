def numbergenerator(userInput):
    addition = 0
    for i in range(0,4):
        temp = 0
        for j in range(0,i+1):
            temp = temp*10 + userInput
        addition = addition + temp       
    return addition 

userIn = int(input("Enter the number: "))
print(numbergenerator(userIn))
#Factorial of a number

def fact(inputNumber):
    if(inputNumber==0):
        return 1
    else:
        return inputNumber*fact(inputNumber-1)

numIn = None
try:
    numIn = int(input("Enter the number: "))
except ValueError as e1:
    print("Invalid input",e1)
finally:
    print(fact(numIn))

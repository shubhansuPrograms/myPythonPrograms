
def operation():
    userInput = list(str(input("Enter the strings separated by comma: ")).split(","))    
    userInput.sort()
    output = ",".join(userInput)
    return output

print(operation())
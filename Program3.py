
def operation(runningNumber,lastNumber):
    if (runningNumber > lastNumber):
        return d
    else:
        d[runningNumber] = runningNumber**2
        
        return operation(runningNumber+1,lastNumber)

d = dict()
finalNumber = int(input("Enter the final number: "))
print(operation(0,finalNumber))
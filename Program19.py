def swap(input1,input2):
    return input2,input1

def insertionSort(inputArray):
    for predator in range(0,len(inputArray)):
        pray = predator+1
        while(pray >= 0):
            if(inputArray[pray]<inputArray[predator]):
                inputArray[pray],inputArray[predator] = swap(inputArray[pray],inputArray[predator])
            else:
                break
            pray = pray - 1
    return inputArray
                


inList = list(str(input("Enter number separated by space")).split(" "))
for i in range(0,len(inList)):
    inList[i] = int(inList[i])

outList = insertionSort(inList)
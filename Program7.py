# creating a matrix

def validityCheck1(input1):
    if(input1.isnumeric()==False):
        pass
    else:
        input1 = int(input1)
    return input1

def matrix(row,column):
    
    lst2 = []
    for i in range(1,row+1):
        lst1 = []
        for j in range(1,column+1):
           lst1.append(i*j)  
        lst2.append(lst1)
        
    return lst2

#Input
rowInput = str(input("Enter the row length: "))
rowInput = validityCheck1(rowInput)
columnInput = str(input("Enter the column length: "))
columnInput = validityCheck1(columnInput)
if(type(rowInput)!= int or type(columnInput) != int or rowInput < 0 or columnInput < 0):
    print("Invalid Entry")
else:
    dimensions = matrix(rowInput,columnInput)
    print(dimensions)
userInput = str(input("Enter the numbers seperated by ,: "))
userList = []
for i in range(0,len(userInput)):
    if(userInput[i].isnumeric()==False):
        pass
    else:
        userList.append(userInput[i])
for i in range(0,len(userList)):
    userList[i] = int(userList[i])

userTupple = tuple(userList.copy())

print (userList)
print (userTupple)
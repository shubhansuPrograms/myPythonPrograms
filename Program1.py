# Program to list all numbers between 2000 to 3200 which are divisible by 7 but not by 5

startNumber = 2000
endNumber = 3201
for startNumber in range(startNumber,endNumber):
    if (startNumber%7 == 0 and startNumber%5 != 0):
        print(startNumber,end = ", ")
    else:
        pass

deposit = 0
withdrawal = 0
balance = 0

while True:
    
    print("Choose from below option: ")
    print("1. Deposit")
    print("2. Withdrawl")
    print("3. Done")
    userOption = str(input("Select an option: "))
    if(userOption.isnumeric() == False or (userOption.isnumeric() == True and int(userOption) not in range(1,4))):
        print("Invalid input")
        break
    else:
        userOption = int(userOption)
        if (userOption == 3):
            balance = deposit - withdrawal
            print("Your balance is: ",balance)
            break
        elif (userOption == 1):
            deposit = deposit + int(input("Enter deposit amount: "))
        elif (userOption == 2):
            withdrawal = withdrawal + int(input("Enter the withdrawl amount: "))
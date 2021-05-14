inLines = []
while True:
    userInput = str(input())
    if (userInput):
        inLines.append(userInput.upper())
    else:
        break

for sentence in inLines:
    print (sentence)
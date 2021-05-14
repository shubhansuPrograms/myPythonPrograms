def operation():
    k = 1
    for i in range(0,7):
        for j in range(0,i+1):
            print(k,end = " ")
            k = k+2
        print()
        if(i>=2 and i%2==0):
            k = k+2
        else:
            k = k + 1

operation()
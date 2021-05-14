from math import *

def operation(C,D,H):
    ans = []
    for i in range(0,len(D)):
        Q = sqrt((2*C*D[i]) // H)
        ans.append(int(Q))
    return ans

D = list(str(input("Enter integer input separated by comma: ")).split(","))
for i in range(0,len(D)):
    D[i] = int(D[i])
C = 50
H = 30
print(operation(C,D,H))

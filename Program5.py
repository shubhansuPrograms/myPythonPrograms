class A:
    def __init__(self):
        self.s = ""

    def getString(self):
        self.s = str(input("Enter the input: "))

    def setString(self):
        print (self.s.upper())

obj1 = A()
obj1.getString()
obj1.setString()
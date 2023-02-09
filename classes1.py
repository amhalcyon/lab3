class sstring:
    def __init__(self):
        self.s1 = ""

    def getString(self):
        self.s1 = input()

    def printString(self):
        print(self.s1.upper())
    
str1 = sstring()
str1.getString()
str1.printString()

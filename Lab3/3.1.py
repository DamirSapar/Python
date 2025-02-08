
# Task 1: Class with methods to get and print a string in uppercase
class StringProcessor:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

# Task 1
sp = StringProcessor()
# sp.getString()  # Uncomment to enter a string manually
# sp.printString() 


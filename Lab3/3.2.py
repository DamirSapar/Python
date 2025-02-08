
# Task 2: Shape class and Square subclass
class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2


# Task 2
s = Square(5)
print("Square area:", s.area())  # Output: 25

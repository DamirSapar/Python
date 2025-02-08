
# Task 3: Rectangle class inheriting from Shape
class Shape:
    def area(self):
        return 0
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Task 3
r = Rectangle(4, 6)
print("Rectangle area:", r.area())  # Output: 24

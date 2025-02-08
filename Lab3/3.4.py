import math


# Task 4: Point class with required methods
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"Point coordinates: ({self.x}, {self.y})")

    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)


# Task 4
p1 = Point(1, 2)
p2 = Point(4, 6)
p1.show()  # Output: (1,2)
p1.move(3, 5)
p1.show()  # Output: (3,5)
print("Distance:", p1.dist(p2))  # Computes distance between p1 and p2

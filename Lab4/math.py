# Exercise 1
import math

degree = float(input("Input degree: "))
radian = degree*(math.pi/180)

print("Output radian: ", f"{radian:.6f}")



# Exercise 2
import math

h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))

print("Expected Output: ", ((a+b)/2)*h)



# Exercise 3
import math

n = float(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

if n < 3 or s <= 0:
    print( "Invalid input: A polygon must have at least 3 sides with positive length.")
else:
    area = (n * s**2) / (4 * math.tan(math.pi / n))

print("The area of the polygon is: ", area)



# Exercise 4
import math

a = float(input("Length of base: "))
h = float(input("Height of parallelogram: "))

print("Expected Output: ", a*h)
# Program to find the area and circumference of a circle

# Input radius from user

import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * (radius ** 2)
circumference = 2 * math.pi * radius

print("\nArea of the circle = {:.2f}".format(area))
print("Circumference of the circle = {:.2f}".format(circumference))

# Program to calculate area of an equilateral triangle

# Input side length from user

import math

side = float(input("Enter the side of the equilateral triangle: "))

area = (math.sqrt(3) / 4) * (side ** 2)

print("\nArea of the equilateral triangle =", area)
